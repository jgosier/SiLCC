"""Provides the BayesTagger class"""
import sys
import csv
import math
import pickle

import nltk

from silcc.lib.basictokenizer import BasicTokenizer
from silcc.lib.util import CIList, capitalization_type

# These should never be tags...
reader = csv.reader(open('data/stopwords.csv'))
stop_words = CIList()
for line in reader:
    stop_words += line

# Grab the trained weights...
print 'Unpickling data...'
unpickle = pickle.load(open('pickle.pickle'))
V = unpickle[0]
C = ['ham', 'spam']
prior = unpickle[1]
condprob = unpickle[2]
print 'Got Unpickled data...'


def featurize(wordpos, context):
    """
    Given a word position within a line of text (the context)
    we return of list of features of the word within the context.
    These features could be the role the word itself
    plays in the context or it could be a feature
    of the context itself, independant of the word.
    """
    features = []
    word = context[wordpos]
    pos = nltk.pos_tag(context)

    # Word is first word __FIRSTWORD__
    if wordpos == 0:
        features.append('__FIRSTWORD__')

    # Word in first 5 words __FIRSTFIVE__
    if wordpos < 5:
        if '__FIRSTFIVE__' not in features:
            features.append('__FIRSTFIVE__')

    # Word in second 5 words __SECONDFIVE__
    if wordpos >= 5 and wordpos < 10:
        if '__SECONDFIVE__' not in features:
            features.append('__SECONDFIVE__')

    # Word is capitilized (first letter is uppercased) __CAPITALIZED__
    if word[0] == word[0].upper():
        if '__CAPITALIZED__' not in features:
            features.append('__CAPITALIZED__')

    # Word is all caps __ALLCAPS__
    if word == word.upper():
        if '__ALLCAPS__' not in features:
            features.append('__ALLCAPS__')

    # All words are all capps __ALLWORDS_ALLCAPS__
    if ' '.join(context) == ' '.join(context).upper():
        if '__ALLWORDS_ALLCAPS__' not in features:
            features.append('__ALLWORDS_ALLCAPS__')

    # Part of Speech __POS_XX__ where XX is POS returned by nltk
    features.append('__POS_%s__' % pos[wordpos][1])

    # Part of Speech previous word __POSPREV_XX__
    if wordpos > 0:
        features.append('__POSPREV_%s__' % pos[wordpos-1][1])

    # Part of Speech next word __POSNEXT_XX__
    if wordpos < (len(context)-1):
        features.append('__POSNEXT_%s__' % pos[wordpos+1][1])

    # Context is a short phrase __SHORT__
    if len(context) < 5:
        features.append('__SHORT__')

    # Context is a long phrase __LONG__
    if len(context) > 10:
        features.append('__LONG__')

    return features


def apply_multinomial_NB(C, V, prior, condprob, d):
    """Returns most likely class"""
    W = d['tokens']
    score = {}
    for c in C:
        score[c] = math.log(prior[c])
        for t in W:
            # if the word has never been seen use 0.4?
            score[c] += math.log(condprob.get((t, c), 0.4))     
    max_score = score['ham']
    max_cat = 'ham'
    for k, v in score.iteritems():
        if v > max_score:
            max_score = v
            max_cat = k
    if score['ham'] > (score['spam'] - 0):
        return 'ham', score
    else:
        return 'spam', score
    return max_cat, score

class BayesTagger(object):
    """
    This class implements a simple tagger that uses
    pre-trained weights to determine most likely
    class for each word in the text.
    """

    @classmethod
    def tag(cls, text):
        """Class method that returns tags given some text"""

        text = text.replace("'", "")
        cap_type = capitalization_type(text)
        bt = BasicTokenizer()

        if cap_type == 'ALLCAPS':
            context = bt.tokenize(text.lower())
        else:
            context = bt.tokenize(text)

        tags = []
        for i in range(len(context)):
            features = featurize(i, context)
            d = dict(
                word=context[i], 
                context=text, 
                features=features, tokens=features, tags=tags)
            m, s = apply_multinomial_NB(C, V, prior, condprob, d)
            if m == 'ham':
                tags.append(context[i])

        # Strip out stopwords...
        tags = [t for t in tags if t not in stop_words]

        # We want to preserve the order of tags purely for esthetic value
        # hence we will not use set()
        # We will also preserve uppercased tags if they are the first occurence

        tags_ = CIList()
        for t in tags:
            if t in tags_: continue
            if len(t) < 2: continue
            tags_.append(t)

        return tags_

if __name__ == '__main__':
    bt = BayesTagger()
    text = sys.argv[1]
    tags = bt.tag(text)
    print tags
