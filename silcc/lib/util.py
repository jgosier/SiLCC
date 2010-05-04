"""Miscellaneous functions and classes"""
import re
import csv

class CIList(list):
    '''
    Case Insensitive list
    A simple derivation of standard list with the
    in operator overridden to make comparisons
    case insensitive.
    '''
    def __contains__(self, key):
        for t in self:
            if key.lower() == t.lower():
                return True
        return False


# These should never be tags...
reader = csv.reader(open('data/stopwords.csv'))
stop_words = CIList()
for line in reader:
    stop_words += line

url_re = re.compile('''
    ^             # we should strip the url first of leading whitespace
    (?:           # non capturing group
    http          # protocols...
    |ftp
    |file
    |mailto
    |gopher
    |news
    |https
    |wais) 
    ://          # protocol / host separator
    (?:www.)?    # we are not interested in leading 'www.' if there...
    ([^:/]*)     # everything up to the first : or / is the host name
    .*           # rest of the url
''', re.VERBOSE | re.IGNORECASE)

def get_host(sburl):
    """returns the host name from a url"""
    s = url_re.search(sburl)
    if s:
        sbhost = s.group(1)
    else:
        sbhost = ''    # did not match url regex
    return sbhost



def capitalization_type(text):
    '''
    Determines the type of capitilzation used:
    NORMAL - Mixture of upper and lower
    ALLCAPS - All words capitilized
    LOWER - All words lower cased
    '''
    tokens = text.split()
    capitilized = [t for t in tokens if t[0].upper() == t[0]]
    if len(capitilized) == 0:
        return 'LOWER'
    elif len(capitilized) == len(tokens):
        return 'ALLCAPS'
    else:
        return 'NORMAL'

def decapitalize_stopwords(text):
    '''
    Converts all stopwords (except first word)
    to leading lowercase word. This is useful for 
    text where all words have been capitalized as the
    POS tagger does not work well on such text.
    '''
    tokens = text.split()
    retval = [tokens[0]]
    for t in tokens[1:]:
        if t in stop_words:
            retval.append(t.lower())
        else:
            retval.append(t)
    return ' '.join(retval)
        
