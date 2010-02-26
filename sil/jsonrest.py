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
	raw = urllib.urlopne(search_url)
	js = raw.readlines()
	js_object = json.loads(js[0])
	
	tweets = []
	for item in js_object['results']:
		user = item['from_user']
		graphic = item['profile_image_url']
		text = item['text']
		time = item['created_at']
		
		thistweet = Tweet(urser,text,graphic,time)
		tweets.append(thistweet)
	return tweets