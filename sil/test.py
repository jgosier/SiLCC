'''
Created on Jan 9, 2010

@author: athena
'''
from MySQLdb import Connect
import nltk
from nltk import pos_tag
from nltk import word_tokenize
from nltk import wordpunct_tokenize
#import random
import re
import feedparser  
import HTMLParser
import MySQLdb
import MySQLdb.cursors
"""
####################
#### Needs      ####
####################
* function to work with populating a table
* function should test whether part of the table has been tagged
* train corpus on handling non-english primitives
"""

class Stripper(HTMLParser.HTMLParser):
    def __init__(self):
        self.reset()
        self.fed=[]
    def handle_data(self,d):
        self.fed.append(d)
    def get_fed_data(self):
        return "".join(self.fed)


    # for links that have the format http://twitter.com/api/cnn
def discreteWord(link):
    s = link.split('/')
    return s[len(s)-1]

    ######################################################
"""This searches the twitter api for current feeds"""    
def replace(self,sw):
    f="http://search.twitter.com/search.atom?q=%s"%sw
    return f
######################################################

def link_to_user(text):
    t = text.split()
    for i in t:
        if i.startswith('@'):
            return "http://twitter.com/"+i
    
def feedObject(search_word):
    f = feedparser.parse("http://search.twitter.com/search.atom?q=%s"%search_word)
    descr = [i.description for i in f.entries]
    newdescr = []
    for j in descr:
        x = Stripper()
        x.feed(j)
        newdescr.append(x.get_fed_data())
    return newdescr
    # function that will extract the url to the user!
    

def searchword(link):
    x = wordpunct_tokenize(link)
    if x[len(x)-1] == 'com':
        return False
    else:
        return x.pop()
    #x = "http://search.twitter.com/vicmiclovich"

    # a function that cleans the string by removing punctuation symbols from name!
def linkify_tweet(tweet):
    tweet = re.sub(r'(\A|\s)@(\w+)',
                   r'\1@<a href="http://www.twitter.com/\2">\2</a>',
                   tweet)
    return re.sub(r'(\A|\s)#(\w+)',
                  r'\1#<a href="http://search.twitter.com/search?q=%23\2">\2</a>',
                  tweet)

    """
        def tokenize(text):
            pattern = r'''(?x)   # strip embedded whitespace
            \w+              # sequences of 'word' characters
            | \$?\d+(\.\d+)? # currency amounts e.g. $12.53
            | (A-Z]\.) +     # abbreviations like U.S.A.
            | [^\w\s]+       # sequences of punctuation
            | \@?\d+(\.\d+)?
            '''
        return nltk.tokenize.regexp_tokenize(text,pattern)
    """

punctuation = re.compile(r'[.,;:!]')

def twitterSearch(feed):
    """
    A twitter is an entity.. denoted by @<some name> e.g. @vicmiclovich, @cnn, etc.
    """
    feed_list = feed.split()
    x = []
    for i in feed_list:
        if i.startswith("@"):
            x.append(punctuation.sub("",i))
        else:
            x.append(None)
    """Implement the part that should strip off all None values to only keep fixed values"""
    y = []
    for i in x:
        if i != None:
            y.append(i)
    if not y:
        return None
    return y[0] # indexed at zero for testing purposes: How would you store a list of tags?
        
def listing(feed):
    """
    This is normally called the hashtag (# tag) by twitter
    """
    feed_list = feed.split()
    x = []
    for i in feed_list:
        if i.startswith("#"):
            x.append(punctuation.sub("",i))
        else:
            x.append(None)
    y = []
    for i in x:
        if i != None:
            y.append(i)
    if not y:
        return None
    return y[0] # indexed at zero for testing purposes; this list usually contents other tags... 
    

def urlsearch(feed):
    """
    A simple function that looks for urls
    """
    x = [i for i in feed.split() if i.startswith("http://")]
    return x


            
def createTag(xdict):
    """
    POS tag??? or should it be a brille tag... 
    This up for debate... with good reason btw!
    """
    tagged_corpus = []
    for title in xdict:
        tagged_corpus.append(pos_tag(word_tokenize(title['title'])))
    return tagged_corpus

def connectToDatabase(host,user,passwd,db):
    """
    This function connects to database returns connection ojbect
    usage:
            >>> conn = <someObject>.connectToDatabase("localhost","j.gosier","morpheus","gregarius")
            >>> cursor = conn.cusor()
    There's an assumption that your are using MySQL
    """
    conn = MySQLdb.connect(
                           host=host,
                           user = user,
                           passwd=passwd,
                           db = db,
                           cursorclass=MySQLdb.cursors.DictCursor)
    return conn





conn1 = connectToDatabase("localhost", "root", "i810du", "greg")

cursor1 = conn1.cursor()
select_sql = "SELECT author, title FROM item"
cursor1.execute(select_sql)

x = cursor1.fetchall() # access item table here
# you can process tags... iteratively
cursor1.close()
conn1.close()

################################
"""List of tokens"""
tc = createTag(x)
#createTag(title,x)
"""
This next part of the code populates another table
You can do other fancy operations with tables such
as performing joins, queries, etc.
conn2 will opens a new connection!
"""

conn2 = connectToDatabase("localhost", "root", "i810du", "greg") 
cursor2 = conn2.cursor()
cursor2.execute("DROP TABLE IF EXISTS test") # access test table
cursor2.execute("CREATE TABLE test (feed TEXT,HashTags TEXT, twitter TEXT)")
for i in range(len(x)):
    cursor2.execute(
                    """
                    INSERT INTO test 
                    VALUES(%s,%s,%s)
                    """,
                    (x[i]['title'],
                    listing(x[i]['title']),
                    twitterSearch(x[i]['title'])
                    )
                )
cursor2.close()
conn2.close()

tagged_list = []
for word in x:
    y = nltk.word_tokenize(word['title'])
    y = [i for i in y if i != 'RT']
    tagged_list.append(nltk.pos_tag(y))

predictive_tag = [] # keywords or more important terms in text
symbols = ['@','#']
"""
The predict tag list might contain hashtags (without the # symbol)...
Should we live it there?

This is the synopis or scene that I want... Suppose you've got a tweet or text

'@j hi, I wish Jane was going to watch the new Harry Potter movie #hollywood with me'

Here for instance the key words (tags) are probably:
Jane, Harry, Potter, hollywood

Should the hashtag "hollywood" be used as tag in this place?

"""
for i in tagged_list:
    predictive_tag.append(
                          list(set([word for word,tag in i if tag == 'NNP' and word not in symbols]))
                          )    

### test whether I get a list of known words
#from pprint import pprint
#pprint(predictive_tag[0])
