import csv

from silcc.lib.sentencetokenizer import SentenceTokenizer

def test_sentencetokenizer():

    tokens = SentenceTokenizer.tokenize("This is a sentence. And this is another.")
    assert tokens == [('FIRST_CAPITALIZED_STOPWORD', 'This'), ('LOWER_STOPWORD', 'is'),
		     ('LOWER_STOPWORD', 'a'), ('LOWER', 'sentence'), ('TERMINATOR', '.'),
                     ('CAPITALIZED_STOPWORD', 'And'), ('LOWER_STOPWORD', 'this'),
                     ('LOWER_STOPWORD', 'is'), ('LOWER', 'another'), ('TERMINATOR', '.')]

    tokens = SentenceTokenizer.tokenize("This Is A Sentence Of Type Allcaps.")
    assert tokens == [('FIRST_CAPITALIZED_STOPWORD', 'This'), ('CAPITALIZED_STOPWORD', 'Is'),
		     ('MIXED_STOPWORD', 'A'), ('CAPITALIZED', 'Sentence'), 
            	     ('CAPITALIZED_STOPWORD', 'Of'), ('CAPITALIZED', 'Type'),
		     ('CAPITALIZED', 'Allcaps'), ('TERMINATOR', '.')]
