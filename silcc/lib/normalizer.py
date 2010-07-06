"""Given short snippet of text converts that text into REGULAR capitilization"""
"""Final Text output is not perfectly formatted around full stop and hiphen"""
import sys
import math
import pickle

from silcc.lib.sentencetokenizer import SentenceTokenizer

unpickle = pickle.load(open('data/weights/capnorm_weights.pickle'))
C = unpickle[0]
V = unpickle[1]
prior = unpickle[2]
condprob = unpickle[3]

class NormalizerException(Exception):
    pass 
    
class Normalizer(object):
    
    def normalizer(self, text):
        
        d = dict(text=text)
        y = SentenceTokenizer.tokenize(d['text'])
        d['tokens'] = [x[0] for x in y]
        result = apply_multinomial_NB(C, V, prior, condprob, d)[0]
        print result
        switch_normalizer = {
        'REGULAR':regular, 
        'GERMAN':german, 
        'ALLCAPS':allcaps, 
        'SHOUT':shout, 
        'LOWER':lower
        }
        text = switch_normalizer.get(result,other)(text,y)
        return text
    


def apply_multinomial_NB(C, V, prior, condprob, d):
    W = d['tokens']
    score = {}
    for c in C:
        score[c] = math.log(prior[c])
        for t in W:
            score[c] += math.log(condprob.get((t, c), 0.4)) # if the word has never been seen use 0.4?
    max_score = score[C[0]]
    max_cat = C[0]
    for k, v in score.iteritems():
        if v > max_score:
            max_score = v
            max_cat = k
    return max_cat, max_score


def regular(text,y):
    '''Convert from Regular to Regular'''
    return text
    
def german(text,y):
    '''Convert from German to German'''
    return text
    
def allcaps(text,y):
    '''Convert from AllCaps to Regular'''
    a = []
    for i, x in enumerate(y):
        a.append(x[1])
        #Add Cap Type Specific Rules
        if (x[0] == 'CAPITALIZED_STOPWORD' or x[0] == 'CAPITALIZED' or x[1] == 'A'):
            a[i] = a[i].lower()
        #End of Rules
    text = ' '.join(a)
    return text
    
def shout(text, d, y):
    '''Convert from shout to Regular'''
    a = []
    for i, x in enumerate(y):
        a.append(x[1])
        #Add Cap Type Specific Rules
        if (x[0] != 'ACRONYM' or x[0] == 'CAPITALIZED'):
            a[i] = a[i].lower()
        #End of Rules
    text = ' '.join(a)
    return text

def lower(text, d, y):
    '''Convert from lower to Regular'''
    a = []
    for i, x in enumerate(y):
        a.append(x[1])
        #Add Cap Type Specific Rules
        if (x[0] == 'CAPITALIZED_STOPWORD' or x[0] == 'CAPITALIZED'):
            a[i] = a[i].lower()
        #End of Rules
    text = ' '.join(a)
    return text

def other(text, d, y):
    '''Leave as it is'''
    return text

if __name__ == '__main__':
    text = sys.argv[1]
    n = Normalizer()
    text = n.normalizer(text)
    print text

  
    
