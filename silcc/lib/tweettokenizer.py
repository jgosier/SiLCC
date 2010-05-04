"""Provides the TweetTokenizer class"""
import re
import sys

class TokenizerException(Exception):
    pass

# Scanner callbacks...
def word_(scanner, token):
    return "WORD", token

def at_name_(scanner, token):
    return "@NAME", token

def colon_(scanner, token):
    return "COLON", token

def url_(scanner, token):
    return "URL", token

def hash_tag_(scanner, token):
    return "#TAG", token

def amp_quote_(scanner, token):
    return "&QUOT", token

def comma_(scanner, token):
    return "COMMA", token

def question_mark_(scanner, token):
    return "QMARK", token

def emoticon_(scanner, token):
    return "EMOTICON", token

def exclamation_(scanner, token):
    return "EXCLAIM", token

def other_(scanner, token):
    return "OTHER", token

def left_paren_(scanner, token):
    return "LEFT_PAREN", token

def right_paren_(scanner, token):
    return "RIGHT_PAREN", token

def dots_(scanner, token):
    return "DOTS", token

def dashes_(scanner, token):
    return "DASHES", token

def percentage_(scanner, token):
    return "PERCENTAGE", token

def dollar_amount_(scanner, token):
    return "DOLLARS", token

def retweet_(scanner, token):
    return "RT", token

def half_word_(scanner, token):
    '''
    "Half" words are words at the end of tweets that 
    have been truncated due to the 140 character limit.
    These words usually end in 2 or more full stops.
    '''
    return "HALFWORD", token


class TweetTokenizer(object):
    """
    TweetTokenizer class provides one 
    class method which tokenizes
    a tweet into suitable format for
    the TweetParser (lexical analysis)
    """


    scanner = re.Scanner([
        ("&amp;", other_),
        (r"/", other_),    
        (r"\;", other_),
        (r"\(", left_paren_),
        (r"\)", right_paren_),
        (r"\.+", dots_),    
        (r"\!", exclamation_),    
        (r":\(", emoticon_),    
        (r":\)", emoticon_),    
        (r":D", emoticon_),
        (r"\,", comma_),    
        (r"\?", question_mark_),    
        (r"#[\w]+", hash_tag_),    
        (r"&quot;", amp_quote_),
        (r"http://[^\s]+", url_),    
        (r"\:", colon_),    
        (r"@\w+", at_name_),
        (r"\b\-+\b", dashes_),    
        (r"\d+\%", percentage_),
        (r"\$[0-9\.,]+", dollar_amount_),
        (r"[A-Za-z0-9'-/]+\.\.+", half_word_),
        (r"\bRT\b", retweet_),
        (r"\b[\w0-9'-/]+\b", word_),
        (r"\s+", None),
        (r"[^\s]", other_)
        ])

    @classmethod
    def tokenize(cls, text):
        tokens, remainder = cls.scanner.scan(text)
        if remainder:
            print "****input failed syntax*****"
            print "tokens:%s" % str(tokens)
            print "remainder:%s" % remainder
            raise TokenizerException
        return tokens



if __name__ == '__main__':
    tweet_text = sys.argv[1]
    tt = TweetTokenizer()
    tokens = tt.tokenize(tweet_text)
    print tokens

