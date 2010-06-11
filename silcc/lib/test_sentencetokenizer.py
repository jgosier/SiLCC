import csv

from silcc.lib.sentencetokenizer import SentenceTokenizer

def test_sentencetokenizer():
    tokens = SentenceTokenizer.tokenize("This is a sentence. And this is another.")
    assert tokens == [
        ('CAPITILIZED', 'This'), ('LOWER', 'is'), ('LOWER', 'a'), 
        ('LOWER', 'sentence'), ('TERMINATOR', '.'), ('CAPITILIZED', 'And'), 
        ('LOWER', 'this'), ('LOWER', 'is'), ('LOWER', 'another'), 
        ('TERMINATOR', '.')]
    tokens = SentenceTokenizer.tokenize("This Is A Sentence Of Type Allcaps.")
    assert tokens == [
        ('CAPITILIZED', 'This'), ('CAPITILIZED', 'Is'), ('MIXED', 'A'), 
        ('CAPITILIZED', 'Sentence'), ('CAPITILIZED', 'Of'), 
        ('CAPITILIZED', 'Type'), ('CAPITILIZED', 'Allcaps'), ('TERMINATOR', '.')]
