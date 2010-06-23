import sys
import re
import readline
import csv
import pickle

from sets import Set
import optparse
import math
import random
from pprint import pprint

from silcc.lib.sentencetokenizer import SentenceTokenizer


def get_training_examples(filename):
    examples = []
    reader = csv.reader(open(filename))
    for line in reader:
        category = line[0]
        text = line[1]
        examples.append(dict(category=category, text=text))
    return examples

def extract_vocabulary(all_entries):
    v = Set()
    for e in all_entries:
        for t in e['tokens']:
            v.add(t)
    return v

def count_docs_in_class(D, c):
    count = 0
    for d in D:
        if d['category'] == c:
            count += 1
    return count

def concatenate_text(D, c):
    retval = []
    for d in D:
        if d['category'] == c:
            for t in d['tokens']:
                retval.append(t)
    return retval

def index(tokens, id, d):
    '''
    Builds an inverted index as follows:
       For each token in tokens, uses that
       as a key in the dict d.
       If the key already exists, then append
       the id (either sbid or sp_id) to the
       list associated with that key. If no 
       list is found then create it.
       e.g.:
       d = {'twitter':[100, 101, 102]}
       Then len(d.get(key)) should give 
       the same result as  Tct = len([token for token in textc if token==t])
       in train_multinomial_NB. (only much faster!)
    '''
    for t in tokens:
        id_list = d.get(t)
        if not id_list:
            d[t] = [id]
        else:
            id_list.append(id)

def train_multinomial_NB_using_indexes(C, D, indexes):
    prior = {}
    condprob = {}
    smoothing_factor = 0.25 # Laplacian = 1, seems to work better at lower values...(requires retraining)
    V = extract_vocabulary(D)
    print 'Size of V: %s' % len(V)
    N = len(D)
    for c in C:
        print c
        category_index = indexes[c]
        Nc = count_docs_in_class(D, c)
        prior[c] = float(Nc) / N
        textc = concatenate_text(D, c)
        count = 0
        for t in V:
            count += 1
            if count % 10000 == 0:
                print count, 'of', len(V) 
            #Tct = len([token for token in textc if token==t])
            Tct = len(category_index.get(t, []))    
            #condprob[(t, c)] =float( Tct + 1.0) / (len(textc) +len(V))
            # Note that after email exchane with Ramesh I added the smoothing factor into the demonimation as well...
            condprob[(t, c)] =float( Tct + smoothing_factor) / (len(textc) + smoothing_factor * len(V))

    return V, prior, condprob

def train_multinomial_NB(C, D):
    prior = {}
    condprob = {}
    smoothing_factor = 0.25 # Laplacian = 1, seems to work better at lower values...(requires retraining)
    V = extract_vocabulary(D)
    print 'Size of V: %s' % len(V)
    N = len(D)
    for c in C:
        print c
        Nc = count_docs_in_class(D, c)
        prior[c] = float(Nc) / N
        textc = concatenate_text(D, c)
        count = 0
        for t in V:
            count += 1
            if count % 1000 == 0:
                print count, 'of', len(V) 
            Tct = len([token for token in textc if token==t])
            #condprob[(t, c)] =float( Tct + 1) / (len(textc) +len(V))
            condprob[(t, c)] =float( Tct + smoothing_factor) / (len(textc) + smoothing_factor * len(V))
    return V, prior, condprob

def apply_multinomial_NB(C, V, prior, condprob, d):
    W = d['tokens']
    score = {}
    for c in C:
        score[c] = math.log(prior[c])
        for t in W:
            score[c] += math.log(condprob.get((t, c), 0.4))     # if the word has never been seen use 0.4?
    max_score = score[C[0]]
    max_cat = C[0]
    for k, v in score.iteritems():
        if v > max_score:
            max_score = v
            max_cat = k
    return max_cat, max_score



if __name__ == '__main__':
    option_parser = optparse.OptionParser()
    option = dict(
        help="Filename of training examples to use (data/training/captypes.csv)", 
        action="store", 
        dest="corpus_filename", 
        type=str,
        default='data/training/captypes.csv')
    option_parser.add_option("--corpus_filename", **option)
    option = dict(
        help="Test the training examples after training.", 
        action="store_true", 
        dest="test", 
        default=False)
    option_parser.add_option("--test", **option)
    (options, args) = option_parser.parse_args()

    '''
    The categories we are training for are:
    'REGULAR'
    'ALLCAPS'
    'LOWER'
    'SHOUT'

    and possibly 'GERMAN'
    '''
    
    # C holds our categories
    C = ['REGULAR', 'ALLCAPS', 'LOWER', 'SHOUT']

    # Now we place all of our training examples into D
    D = get_training_examples(options.corpus_filename)

    # Now extract the features for the trainer...
    for d in D:
        d['tokens'] = [x[0] for x in SentenceTokenizer.tokenize(d['text'])]

    print 'Training...'
    V, prior, condprob = train_multinomial_NB(C, D)

    # Now pickle these for use by capnormalizer
    stuff_to_pickle = (C, V, prior, condprob)
    print 'Pickling...'
    pickle.dump(stuff_to_pickle, open('data/weights/capnorm_weights.pickle', 'wb'))
    print 'Done.'

    if options.test:
        # Now test the training examples as well, 
        # most should give correct category if training went well...
        for d in D:
            result = apply_multinomial_NB(C, V, prior, condprob, d)
            print d
            print result

