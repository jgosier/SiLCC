# Author: victor miclovich
# This script is for testing purposes only
# only parts of it will make up SiLCC

import json, urllib

class Tweet():
	def __init__(self,user,text,graphic,time):
		self.user = user
		self.text = text
		self.graphic = graphic
		self.time = time

def search_twitter():
	search_url = 'http://search.twitter.com/search.json?q=Django'

	raw = urllib.urlopen(search_url)
	print "Read off search URL..."
	js = raw.readlines()
	print "transferred all data to js"
	js_object = json.loads(js[0])
	print "loading json object complete"
	tweets = []
	for item in js_object['results']:
		user = item['from_user']
		graphic = item['profile_image_url']
		text = item['text']
		time = item['created_at']		
		thistweet = Tweet(user,text,graphic,time)
		tweets.append(thistweet)
	return tweets

x = search_twitter()
for i in x:
	print i.text
	print i.graphic
	print i.time