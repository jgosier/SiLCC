'''
Created on Feb 25, 2010

@author: athena
'''
# -*- coding: utf-8 -*-

import random, nltk, string

# NLP work
def generateTweetTokens(jsonfile):
	tweets = [nltk.word_tokenize(json.loads(i)['text']) for i in open(jsonfile)]
	random.shuffle(tweets)

def freqDistributionTweetWords(tweets):
    # tweets is a list
	allWords = nltk.FreqDist(word.lower()
						for item in tweets
						for word in item 
						if word not in string.punctuation and word not in string.digits and word not in string.whitespace)
						
	partitioner = len(allWords)
	wordFeatures = allWords.keys()[:partitioner/2] # figure should not be small i.e. 100

def tweet_features(tweet):
	# tweet is already tokenized
	tweetWords = set(tweet)
	features = {}
	for word in wordFeatures:
		features['contains(%s)'%word] = (word in tweetWords)
	return features

def buildFeatureset(tweetcorpus):
	#
	pass

# take in a training set and return a classifier object
def classify(training_set):
	classifier = nltk.NaiveBayesClassifier.train(training_set)
	return classifier # classifier object

def predict(tweet_token,classifier):
	# This function helps predict
	return classifier.classify(tweet_token)

