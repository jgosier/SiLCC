"""Given short snippet of text converts that text into REGULAR capitilization"""
#"""Final Text output is not perfectly formatted around full stop and hiphen"""
import sys
import math
import pickle

from silcc.lib.sentencetokenizer import SentenceTokenizer
from sqlalchemy import select, and_, create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from paste.deploy import appconfig
from pylons import app_globals
from silcc.config.environment import load_environment
from sqlalchemy import select, and_, create_engine, MetaData
import sqlalchemy as sa


unpickle = pickle.load(open('data/weights/capnorm_weights.pickle'))
C = unpickle[0]
V = unpickle[1]
prior = unpickle[2]
condprob = unpickle[3]

class NormalizerException(Exception):
    pass 
    
class Normalizer(object):
    """Normalizer class for which instance should be created"""
    
    def normalizer(self, text):
        """To be called with the text string and returns normalized version"""
        
        dt_ = dict(text=text)
        ya_ = SentenceTokenizer.tokenize(dt_['text'])
        dt_['tokens'] = [xb_[0] for xb_ in ya_]
        result = apply_multinomial_NB(C, V, prior, condprob, dt_)[0]
        
        #print result
        
        switch_normalizer = {
        'REGULAR' : regular, 
        'GERMAN' : german, 
        'ALLCAPS' : allcaps, 
        'SHOUT' : shout, 
        'LOWER' : lower }
        text = switch_normalizer.get(result, other)(text, ya_)
        return text.replace(' .', '.')
    


def apply_multinomial_NB(C, V, prior, condprob, dt_):
    W = dt_['tokens']
    score = {}
    for c in C:
        score[c] = math.log(prior[c])
        for t in W:
            # if the word has never been seen use 0.4?
            score[c] += math.log(condprob.get((t, c), 0.4)) 
    max_score = score[C[0]]
    max_cat = C[0]
    for k, v in score.iteritems():
        if v > max_score:
            max_score = v
            max_cat = k
    return max_cat, max_score


def regular(text, ya_):
    '''Convert from Regular to Regular'''
    return text
    
def german(text, ya_):
    '''Convert from German to German'''
    return text
    
def allcaps(text, ya_):
    '''Convert from AllCaps to Regular'''
    ab_ = []
    for i, xb_ in enumerate(ya_):
        ab_.append(xb_[1])
        #Add Cap Type Specific Rules
        if (xb_[0] == 'CAPITALIZED_STOPWORD' or 
            xb_[0] == 'CAPITALIZED' or xb_[1] == 'A'):
            ab_[i] = ab_[i].lower()
        #End of Rules
    text = ' '.join(ab_)
    return text
    
def shout(text, ya_):
    '''Convert from shout to Regular'''
    text = text.lower()
    ab_ = []
    for i, xb_ in enumerate(ya_):
        ab_.append(xb_[1])
        #Add Cap Type Specific Rules
        if (xb_[0] != 'ACRONYM'):
            ab_[i] = ab_[i].lower()
        if (xb_[0] == 'FIRST_SHOUT_STOPWORD' or xb_[0] == 'FIRST_SHOUT'):
            ab_[i] = ab_[i].capitalize()
        

        
        #End of Rules
    text = ' '.join(ab_)
    return text
    
def lower(text, ya_):
    '''Convert from lower to Regular'''
    ab_ = []
    for i, xb_ in enumerate(ya_):
        ab_.append(xb_[1])
        #Add Cap Type Specific Rules
        if (xb_[0] == 'FIRST_LOWER_STOPWORD' or xb_[0] == 'FIRST_LOWER'):
            ab_[i] = ab_[i].capitalize()
        if (xb_[0] == 'ACRONYM'):
            ab_[i] = ab_[i].upper()

        
        
        #End of Rules
    text = ' '.join(ab_)
    return text

def other(text, ya_):
    '''Leave as it is'''
    return text

if __name__ == '__main__':
    text = sys.argv[1]
    N = Normalizer()
    print N.normalizer(text)


  
    
