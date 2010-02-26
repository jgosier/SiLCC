'''
Created on Jan 8, 2010

@author: athena
'''
# -*- coding: utf-8 -*-

import feedparser
import urllib
import json
from string import punctuation
import nltk

class Stripper(HTMLParser.HTMLParser):
    def __init__(self):
        self.reset()
        self.fed=[]
    def handle_data(self,d):
        self.fed.append(d)
    def get_fed_data(self):
        return "".join(self.fed)

class Data():
	def __init__(self,text):
		self.text = text

# using the call_uri function... SiLCC waits for link with a json resource
# it reads of the JSON inside of the link... and populates text
def call_uri(uri):

	search_url = '%s'%uri
	raw = urllib.urlopen(search_url)
	print "Read off search URL..."
	js = raw.readlines()
	print "transferred all data to js"
	js_object = json.loads(js[0])
	print "loading json object complete"
	tweets = []
	for item in js_object['results']:
		text = item['text']
		thistweet = Tweet(text)
		tweets.append(thistweet)
	return tweets


class Utilities:
    def __init__(self,folder):
        self.folder = folder
    def parselink(self, link):
        return feedparser.parse(link)

    """Generates file name"""
    def filename(self,parse):
        filename = "".join(i for i in nltk.word_tokenize(parse.feed.values()[0])[:5] if i not in punctuation and i != "GMT")+".txt"
        return filename

    def saveToFile(self, p,fname):
        file = open('%s/'%(self.folder)+fname,'w')
        entry_list = []
        for i in range(len(p.entries)):
            entry_list.append((p.entries[i].title,nltk.clean_html(p.entries[i].description)))

        for t,d in entry_list:
            file.write(t+'\n'+d+'\n')
        file.close()

    def corpusGenerate(self,rss_links):
        for i in rss_links:
            file_name = i + self.filename(self.parselink(rss_links[i]))
            self.saveToFile(self.parselink(rss_links[i]), file_name)
            
    '''JSON parser'''     
    def parseJSON(uri):
    	# get the URI and extract json object
    	items = json.loads(uri) # uri is just a json object
    	# items are just the things we return for every 
    	# iteration through json lines
    	return items
    	

def searchword(link):
    x = nltk.wordpunct_tokenize(link)
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
    A simple function that looks for urls in a feed
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

def predictive_tags(tweet)
	tagged_list = []
	tweet_tokens = nltk.word_tokenize(tweet)
	tagged_tokens = nltk.pos_tag(tweet_tokens)
	
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
   	