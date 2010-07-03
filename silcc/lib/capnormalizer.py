"""Given short snippet of text converts that text into REGULAR capitilization"""
import sys
import math
import pickle

from silcc.lib.sentencetokenizer import SentenceTokenizer

unpickle = pickle.load(open('data/weights/capnorm_weights.pickle'))
C = unpickle[0]
V = unpickle[1]
prior = unpickle[2]
condprob = unpickle[3]

class CapType(object):
    """Namespace for Capitilzation Type Constants"""
    REGULAR = 0
    GERMAN = 1
    ALLCAPS = 2
    SHOUT = 3
    LOWER = 4
    OTHER = 5

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

def capitalization_type(text):
    """Determine the capilitization type of the text
Types are:

- REGULAR: First letter of First word in sentences
is capitilized as well as first letter of proper nouns.

- GERMAN: First letter of First word in sentences as
well as first letter of any noun.

- ALLCAPS: First letter of every word is capitilized.
- SHOUT: Every letter is uppercase.

- LOWER: Every letter is lowercase.

- OTHER: None of the above definitions apply.
(This may also mean mixed type)

"""
    d = dict(text=text)
    d['tokens'] = [x[0] for x in SentenceTokenizer.tokenize(d['text'])]
    result = apply_multinomial_NB(C, V, prior, condprob, d)
    result = result[0]
    type_map = dict(
        REGULAR=CapType.REGULAR,
        GERMAN=CapType.GERMAN,
        ALLCAPS=CapType.ALLCAPS,
        SHOUT=CapType.SHOUT,
        LOWER=CapType.LOWER,
        OTHER=CapType.OTHER
        )
    return type_map[result]

if __name__ == '__main__':
    text = sys.argv[1]
    type_ = capitalization_type(text)
    for k, v in CapType.__dict__.iteritems():
        if isinstance(v, int) and type_ == v:
            print k

