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

def append_word(current_state, d, token, next_state):
    '''
    Adds a WORD token to the text list.
    '''
    text = d.get('text', [])
    if not text:
        d['text'] = [token[1]]
    else:
        text.append(token[1])


def append_hashtag(current_state, d, token, next_state):
    '''
    Adds a HASHTAG token to the hashtag list.
    '''
    hashtags = d.get('hashtags', [])
    if not hashtags:
        d['hashtags'] = [token[1]]
    else:
        hashtags.append(token[1])

class ParserException(Exception):
    """Raised if the Parser fails to find an appropriate rule"""
    pass


class CapTypeDetector(object):
    '''
    Determines the capitilzation type.
    '''

    #      STATE          TOKEN          ACTION               NEXT_STATE  
    parse_rules = (
        ( 'START',       'CAPITALIZED',  None,               'ALLCAPS' ),
        ( 'START',       'UPPER',        None,               'SHOUT' ),
        ( 'START',       'MIXED_CAPITALIZED',  None,         'ALLCAPS' ),
        ( 'ALLCAPS',     'CAPITALIZED',  None,               'ALLCAPS' ),
        ( 'ALLCAPS',     'TERMINATOR',   None,               'ALLCAPS' ),
        ( 'ALLCAPS',     'OTHER',        None,               'ALLCAPS' ),
        ( 'ALLCAPS',     'LOWER',        None,               'REGULAR' ),
        ( 'ALLCAPS',     'MIXED_CAPITALIZED',  None,         'ALLCAPS' ),
        ( 'REGULAR',     'LOWER',        None,               'REGULAR' ),
        ( 'REGULAR',     'MIXED',        None,               'REGULAR' ),
        ( 'REGULAR',     'MIXED_CAPITALIZED',        None,               'REGULAR' ),
        ( 'REGULAR',     'CAPITALIZED',        None,               'REGULAR' ),
        )


    @classmethod
    def parse(cls, text, debug=True):
        """Class method that returns a parsing of text from a tweet"""
        d = dict()
        STATE = 'START'
        tokens, remainder = SentenceTokenizer.scanner.scan(text)
        for t in tokens:
            current_token = t
            found_rule = False
            for r in cls.parse_rules:
                if r[0] == STATE and r[1] == current_token[0]:
                    found_rule = True
                    if debug:
                        print 'Applying: State:%s Token:%s Action:%s \
Next State:%s to token %s' % (r[0], r[1], r[2], r[3], current_token[1])
                    callback = r[2]
                    next_state = r[3]
                    if callback:
                        callback(STATE, d, current_token, next_state)
                    STATE = next_state
                    break
            if not found_rule:
                print text
                print '******* NO rule for token:%s state: %s' % \
                (current_token, STATE)
                raise ParserException
        type_map = dict(
            REGULAR=CapType.REGULAR,
            GERMAN=CapType.GERMAN,
            ALLCAPS=CapType.ALLCAPS,
            SHOUT=CapType.SHOUT,
            LOWER=CapType.LOWER,
            OTHER=CapType.OTHER
         )
        return type_map[STATE]


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

    sd = CapTypeDetector()
    type_ = CapType.OTHER
    type_ = sd.parse(text)
    return type_


if __name__ == '__main__':
    text = sys.argv[1]
    type_ = capitalization_type(text)
    for k, v in CapType.__dict__.iteritems():
        if isinstance(v, int) and type_ == v:
            print k
