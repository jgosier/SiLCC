"""Given short snippet of text converts that text into REGULAR capitilization"""
import sys
from silcc.lib.sentencetokenizer import SentenceTokenizer

class CapType(object):
    """Namespace for Capitilzation Type Constants"""
    REGULAR = 0
    GERMAN = 1
    ALLCAPS = 2
    SHOUT = 3
    LOWER = 4
    OTHER = 5

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
    tokens, remainder = SentenceTokenizer.scanner.scan(text)
    weights = {
        'REGULAR':{'CAPITALIZED_STOPWORD': 0.1, 'LOWER_STOPWORD':0.8, 'CAPITALIZED': 0.3, 'SHOUT':0.4 },
        'ALLCAPS':{'CAPITALIZED_STOPWORD': 0.9, 'LOWER_STOPWORD':0.1 },
        'LOWER': {'FIRST_LOWER': 0.9, 'FIRST_LOWER_STOPWORD': 0.9, 'LOWER_STOPWORD':0.6, 'CAPITALIZED_STOPWORD': 0.05, 
                  'LOWER':0.6, 'SHOUT':0.1, 'CAPITALIZED': 0.1  },
        'SHOUT': {'SHOUT': 0.8, 'LOWER_STOPWORD': 0.1, 'LOWER': 0.01 }
    }
    scores = {}
    for cap_type, cap_type_weights in weights.iteritems():
        score = 1
        for token in tokens:
            score *= cap_type_weights.get(token[0], 0.5)
        scores[cap_type] = score
    deco_scores = [(v, k) for k, v in scores.iteritems()]
    deco_scores.sort(reverse=True)
    type_map = dict(
        REGULAR=CapType.REGULAR,
        GERMAN=CapType.GERMAN,
        ALLCAPS=CapType.ALLCAPS,
        SHOUT=CapType.SHOUT,
        LOWER=CapType.LOWER,
        OTHER=CapType.OTHER
        )
    return type_map[deco_scores[0][1]]

if __name__ == '__main__':
    text = sys.argv[1]
    type_ = capitalization_type(text)
    for k, v in CapType.__dict__.iteritems():
        if isinstance(v, int) and type_ == v:
            print k
