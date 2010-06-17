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
    def upper_(scanner, token):
        if token in stop_words:
            return "UPPER_STOPWORD", token
        else:
            return "UPPER", token

    def lower_(scanner, token):
        if token in stop_words:
            return "LOWER_STOPWORD", token
        else:
            return "LOWER", token

    def capitalized_(scanner, token):
        """Capitalized means the first letter is upper only"""
        if token in stop_words:
            return "CAPITALIZED_STOPWORD", token
        else:
            return "CAPITALIZED", token

    def first_capitalized_(scanner, token):
        """For the first word in a report"""
        return "FIRST_CAPITALIZED", token

    def shout_(scanner, token):
        """All chars are upper"""
        return "SHOUT", token

    def first_lower_(scanner, token):
        """For the first word in a report"""
        return "FIRST_LOWER", token

    def mixed_(scanner, token):
        return "MIXED", token

    def mixed_capitalized_(scanner, token):
        return "MIXED_CAPITALIZED", token

    def other_(scanner, token):
        return "OTHER", token

    def terminator_(scanner, token):
        """Any token that indicates end of sentence e.g. . and ? """
        return "TERMINATOR", token

    def spaces_(scanner, token):
        """Any token that indicates end of sentence e.g. . and ? """
        return "SPACES", token


    scanner = re.Scanner([
        (r"\b[A-Z][A-Z]+\b", shout_),    
        (r"^[A-Z][a-z\-]+\b", first_capitalized_),
        (r"^[a-z\-]+\b", first_lower_),
        (r"\b[A-Z][a-z\-]+\b", capitalized_),
        (r"\b[a-z]+\b", lower_),
        (r"\b[A-Z][A-Za-z\-]+\b", mixed_capitalized_),
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


