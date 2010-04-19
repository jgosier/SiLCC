import logging
import sys

import nltk
from sqlalchemy import and_, desc, func, or_, select

from silcc.model import Place
from silcc.model.meta import Session
from silcc.lib.HeadlineTokenizer import HeadlineTokenizer

log = logging.getLogger(__name__)

# nltk POS codes:
# NN - noun
# NNP - proper noun
# NNS - plural noun
# VBD - verb 

pos_include = ('NN', 'NNP', 'NNS')

# These should never be tags...
stop_words = ('a', 'an','and','at', 'are','as',
              'be', 'by','but',
              'can',
              'do', 'does', 'done','did',"didn't",
              'for','from',
              'go', 'get',
              'he', 'his','how','had','has',"he's", 'her', 'hers',
              'in', "i'm", "i'll",'is', 'it', 'im',"iv'e",'if','its',
              'my',
              'no', 
              'of','on','our','or',
              'rt',
              'so', 'she',
              'to','the','then', 'there','than', 'that','this',
              'us','up',
              'we','who','with','was','will','when','why',
              "you'll", 'you',
              '-', '--', '---'
              )

def capitilization_type(text):
    '''
    Determines the type of capitilzation used:
    NORMAL - Mixture of upper and lower
    ALLCAPS - All words capitilized
    LOWER - All words lower cased
    '''
    tokens = text.split()
    capitilized = [t for t in tokens if t[0].upper() == t[0]]
    log.info('Capitilized tokens: %s', str(capitilized))
    if len(capitilized) == 0:
        return 'LOWER'
    elif len(capitilized) == len(tokens):
        return 'ALLCAPS'
    else:
        return 'NORMAL'
                 

def extract_tags(text):

    cap_type = capitilization_type(text)

    ht = HeadlineTokenizer()
    #tokens = ht.tokenize(text.replace("'",""))
    tokens = ht.tokenize(text)
    pos = nltk.pos_tag(tokens)
    log.info('POS before lower casing:%s', str(pos))

    if cap_type == 'ALLCAPS':
        # If the headline is in AllCAPS then the POS tagger
        # produces too many proper nouns, hence we de-capitilize text first
        tokens = ht.tokenize(text.lower())
        pos = nltk.pos_tag(tokens)
        log.info('POS after lower casing:%s', str(pos))

    # Only return those tokens whose pos is in the include list
    tags = [t[0] for t in pos if t[1] in pos_include and not t[0].lower() in stop_words]

    # We want to preserve the order of tags purely for esthetic value
    # hence we will not use set()

    tags_ = []
    for t in tags:
        if t in tags_: continue
        tags_.append(t)

    return tags_


if __name__ == '__main__':
    text = sys.argv[1]
    tags = extract_tags(text)
    print tags
