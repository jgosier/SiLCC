"""Tokenizes sentences into word types for capitilzation detection"""
import re
import sys

from silcc.lib.basictagger import stop_words

class TokenizerException(Exception):
    pass

class SentenceTokenizer(object):

    '''
    Tokenizer for News/Blog headlines that
    returns words with a capitilization type.
    Ignores most punctuation except for 
    sentence termination characters such
    as full stops and question marks.
    '''


    # Scanner callbacks...
    '''
    Redundant
   def upper_(scanner, token):
        if token in stop_words:
            return "UPPER_STOPWORD", token
        else:
            return "UPPER", token
    '''

    def lower_(scanner, token):
        if token in stop_words:
            return "LOWER_STOPWORD", token
        else:
            return "LOWER", token
    
    def lower_stop_(scanner, token):
        return "LOWER_STOP", token
        
    
    def capitalized_(scanner, token):
        """Capitalized means the first letter is upper only"""
        if token in stop_words:
            return "CAPITALIZED_STOPWORD", token
        else:
            return "CAPITALIZED", token
            
    def capitalized_stop_(scanner, token):
        return "CAPITALIZED_STOP", token


    def first_capitalized_(scanner, token):
        """For the first word in a report"""
        if token in stop_words:
            return "FIRST_CAPITALIZED_STOPWORD", token
        else:
            return "FIRST_CAPITALIZED", token

    def first_capitalized_stop_(scanner, token):
        return "FIRST_CAPITALIZED_STOP", token


    def shout_(scanner, token):
        """All chars are upper"""
        if token in stop_words:
            return "SHOUT_STOPWORD", token
        else:
            return "SHOUT", token
    
    def shout_stop_(scanner, token):
        return "SHOUT_STOP", token


    def first_lower_(scanner, token):
        """For the first word in a report"""
        if token in stop_words:
            return "FIRST_LOWER_STOPWORD", token
        else:
            return "FIRST_LOWER", token
    
    def first_lower_stop_(scanner, token):
        return "FIRST_LOWER_STOP", token
    
    
    def mixed_(scanner, token):
        """tHis is mixed, so is tHIs"""
        if token in stop_words:
            return "MIXED_STOPWORD", token
        else:
            return "MIXED", token
    
    def mixed_stop_(scanner, token):
        return "MIXED_STOP", token

    
    def mixed_capitalized_(scanner, token):
        if token in stop_words:
            return "MIXED_CAPITALIZED_STOPWORD", token
        else:
            return "MIXED_CAPITALIZED", token
    
    def mixed_capitalized_stop_(scanner, token):
        return "MIXED_CAPITALIZED_STOP", token
    

    def other_(scanner, token):
        if token in stop_words:
            return "OTHER_STOPWORD", token
        else:
            return "OTHER", token

    
    def terminator_(scanner, token):
        """Any token that indicates end of sentence e.g. . and ? """
        return "TERMINATOR", token

    
    def spaces_(scanner, token):
        """Any token that indicates end of sentence e.g. . and ? """
        return "SPACES", token


    scanner = re.Scanner([
        (r"\b[A-Z][A-Z]+(ED|LY|ING|IZE)\b", shout_stop_), 
        (r"\b[A-Z][A-Z]+\b", shout_),    
        (r"^[A-Z][a-z\-]+(ed|ly|ing|ize)\b", first_capitalized_stop_),
        (r"^[A-Z][a-z\-]+\b", first_capitalized_),
        (r"^[a-z\-]+(ed|ly|ing|ize)\b", first_lower_stop_),
        (r"^[a-z\-]+\b", first_lower_),
        (r"\b[A-Z][a-z\-]+(ed|ly|ing|ize)\b", capitalized_stop_),
        (r"\b[A-Z][a-z\-]+\b", capitalized_),
        (r"\b[a-z]+(ed|ly|ing|ize)\b", lower_stop_),
        (r"\b[a-z]+\b", lower_),
        # big enough to ingore pylint's 80 char warning
        # getting the expression below to work in one go is an achievement 
        (r"\b[A-Z][A-Za-z\-]+(((e|E)(d|D))|((l|L)(y|Y))|((i|I)(n|N)(g|G))|((i|I)|(z|Z)|(e|E)))\b", mixed_capitalized_stop_),
        (r"\b[A-Z][A-Za-z\-]+\b", mixed_capitalized_),
        (r"\b[A-Za-z]+(((e|E)(d|D))|((l|L)(y|Y))|((i|I)(n|N)(g|G))|((i|I)|(z|Z)|(e|E)))\b", mixed_stop_),
        (r"\b[A-Za-z]+\b", mixed_),
        (r"[\.\?]", terminator_),
        # This rule is for tokens containing non letters or mixtures
        # of non-letters and letters for which cap type makes no sense
        # for example: $52k, R101, s26 etc 
        (r"[^\s]+", other_),
        (r"\s+", None),
        ])

    @classmethod
    def tokenize(cls, text):
        tokens, remainder = cls.scanner.scan(text)
        if remainder:
            print "****input failed syntax*****"
            print "tokens:%s" % str(tokens)
            print "remainder:%s" % remainder
            raise TokenizerException
        #include = ("WORD",)
        #tokens = [t[1] for t in tokens if t[0] in include]
        return tokens

if __name__ == '__main__':
    text = sys.argv[1]
    st = SentenceTokenizer()
    print text
    tokens = st.tokenize(text)
    print tokens


