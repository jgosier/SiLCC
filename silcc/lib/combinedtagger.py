"""Provides a class that will parse and tag text from a single tweet""" 
import sys

from silcc.lib.util import CIList
from silcc.lib.basictagger import BasicTagger
from silcc.lib.bayestagger import BayesTagger

class CombinedTagger(object):
    """
    This tagger outputs the union of the tags from                                                                                 
    BasicTagger and from BayesTagger. It sometimes gives better
    results than either of the two taggers alone

    for example:
       "The Size Of The African Blogosphere
        According To Afrigator The African
        Aggregrator"

    Basic: ['size', 'blogosphere', 'afrigator', 'aggregrator']
    Bayes: ['size', 'african', 'blogosphere', 'aggregrator']
    Combined: ['size', 'blogosphere', 'afrigator', 'aggregrator', 'african']

                                                                                                                  
    """

    @classmethod
    def tag(cls, text):
        """Class method that returns tags given some text"""
        combined_tags = BasicTagger.tag(text)
        combined_tags += BayesTagger.tag(text)
        tags = CIList()
        for tag in combined_tags:
            if tag not in tags:
                tags.append(tag)
        return tags


if __name__ == '__main__':
    text = sys.argv[1]
    tags = CombinedTagger.tag(text)
    print tags




    
