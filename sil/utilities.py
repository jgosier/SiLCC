'''
Created on Jan 8, 2010

@author: athena
'''
# -*- coding: utf-8 -*-

import feedparser
from string import punctuation
import nltk
class Utilities:
    def __init__(self,folder):
        self.folder = folder
    def parselink(self, link):
        return feedparser.parse(link)

    """Generates file name"""
    def filename(self,parse):
        filename = "".join(i for i in nltk.word_tokenize(parse.feed.values()[0])[:5] if i not in punctuation and i != "GMT")+".txt"
        return filename

    def saveToFile(self, p,fname):
        file = open('%s/'%(self.folder)+fname,'w')
        entry_list = []
        for i in range(len(p.entries)):
            entry_list.append((p.entries[i].title,nltk.clean_html(p.entries[i].description)))

        for t,d in entry_list:
            file.write(t+'\n'+d+'\n')
        file.close()

    def corpusGenerate(self,rss_links):
        for i in rss_links:
            file_name = i + self.filename(self.parselink(rss_links[i]))
            self.saveToFile(self.parselink(rss_links[i]), file_name)