'''
Created on Jan 13, 2010

@author: athena
'''
#classifies by brute force
"""
This whole script has got utilities or functions that handle generation of various
kinds of corpora!

The architecture:
*This data can be the data that we trust, we should use a list of sites that we believe give more genuine information
*Then, I believe that by using this data we can extract relevent words, do relevant data analyses.
"""
import os

from utilities import Utilities

os.chdir("newscorpus")

def start():
    
    science = {
           "BBC_science":"http://newsrss.bbc.co.uk/rss/newsonline_world_edition/science/nature/rss.xml",
           "USNEWS_science":"http://www.usnews.com/rss/science/index.rss"
           }
    sci = Utilities('science')
    sci.corpusGenerate(science)

    sports = {
          "CNN sports":"http://rss.cnn.com/rss/si_topstories.rss"
          }
    sprts = Utilities('sports')
    sprts.corpusGenerate(sports)

    business = {
            "BBC_business":"http://newsrss.bbc.co.uk/rss/newsonline_world_edition/business/rss.xml",
            "CNN_business":"http://rss.cnn.com/rss/money_latest.rss",
            "USNEWS_money":"http://www.usnews.com/rss/business/index.rss"
            }
    bz = Utilities('business')
    bz.corpusGenerate(business)

    technology = {
              "technology":"http://newsrss.bbc.co.uk/rss/newsonline_world_edition/technology/rss.xml",
              }
    tch = Utilities('technology')
    tch.corpusGenerate(technology)

    entertainment = {
                 "BBC_entertainment":"http://newsrss.bbc.co.uk/rss/newsonline_world_edition/entertainment/rss.xml"
                 }

    ent = Utilities('entertainment')
    ent.corpusGenerate(entertainment)

"""Callable script with start()"""
if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        print "Wow... !!!!"
