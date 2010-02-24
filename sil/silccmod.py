import random, nltk, json, string

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
	
def classify(trainset):
	classifier = nltk.NaiveBayesClassifier.train(trainset)
	return classifier # classifier object

def predict(tweet):
	# This function helps predict
	pass

'''Tests'''
partTweet = len(tweets)

# In this part I assumend that have the tweets are true facts
# the other half was false..
# this is just for testing purposes... using the "words-in-bag" model 
# and it is a very bad model

test_truthy = tweets[:partTweet/2]
test_falsy = tweets[partTweet/2:]
tweetcorpus = [(tt,'truthy') for tt in test_truthy] + [(tf, 'falsy') for tf in test_falsy]
random.shuffle(tweetcorpus)

featuresets = [(tweet_features(tWords),c) for (t,c) in tweetcorpus
										for tWords in t]

partFeaturesets = len(featuresets)
train_set = featuresets[partFeaturesets/2:]
test_set = featuresets[:partFeaturesets/2]

# Why isn't this working well enough?
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier,test_set)
print
print
classifier.show_most_informative_features()