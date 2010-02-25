import couchdb
from couchdb.client import Server
from couchdb.schema import IntegerField, TextField, Document
import json
import time

# chat with the couchdb server

class Tweet(Document):
	id = IntegerField()
	from_user = TextField()
	text = TextField()
	
# TODO optimize for speed... very verbose
j = open('geotagged_tweets_from_haiti.json')
# open json objects
jsonobjects = [i for i in j]

l = [json.loads(j) for j in jsonobjects]

server = Server('http://127.0.0.1:5984')
try:
	db = server.create('tweetgeneral')
except:
	del server['tweetgeneral']
	db = server.create('tweetgeneral')
	
# for each_tweet in l:
# 	tweet = Tweet(id=each_tweet['id'],from_user=each_tweet['from_user'],text=each_tweet['text'])
# 	tweet.store(db)
# 	


