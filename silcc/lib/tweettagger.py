"""Provides a class that will parse and tag text from a single tweet""" 
import sys

from silcc.lib.tweetparser import TweetParser
from silcc.lib.basictagger import BasicTagger
from silcc.lib.bayestagger import BayesTagger

class TweetTagger(object):
    """
    TweetTagger class provides a class with a static
    method called "tag" which can be used to tag
    a single tweet. It may also be used for news headlines
    since these are generally a subset of tweets.
    """

    @classmethod
    def tag(cls, tweet, texttagger=BasicTagger, debug=False):
        """Class method to tag a tweet or other text."""

        parsed_tweet = TweetParser.parse(tweet, debug=debug)
        text = parsed_tweet.get('text')
        tags = texttagger.tag(text)

        # Now add the hashtags from the parsing...
        hashtags = parsed_tweet.get('hashtags', [])
        # Strip off the '#'...
        hashtags = [h[1:] for h in hashtags]
        for tag in hashtags:
            if tag in tags: 
                continue
            tags.append(tag)
        return tags

if __name__ == '__main__':
    tweet = sys.argv[1]
    tags = TweetTagger.tag(tweet, texttagger=BasicTagger)
    print "Basic:", tags
    tags = TweetTagger.tag(tweet, texttagger=BayesTagger)
    print "Bayes:", tags






    
