'''
Created on Jan 8, 2010

@author: athena
'''
# -*- coding: utf-8 -*-
#import utilities
import twitter
import tweepy
#import sqlite3
import os

#import time
from textwrap import TextWrapper
#####################
"""TEST LIBRARIES"""
from test import feedObject


os.chdir('twittercontent')

#conn = sqlite3.connect('cont.db')
#c = conn.cursor()
search_words = ["haiti-boots-on-ground","live-from-haiti",]
             
#fil = open("content.pkl",'wb')


"""TEST PORTION """
emp = [] # keep lists of dicts!
for i in search_words:
    emp.append(feedObject(i))

#count = 0
#for i in emp:
#    for j in i:
#        count += 1
#print count

##################################
 
"""
http://twitter.com/CNN/haiti-boots-on-ground

http://twitter.com/georgiap/live-from-haiti

http://twitter.com/jilliancyork/haiti

#http://twitter.com/haiti use api

#http://twitter.com/InternetHaiti use api

#http://twitter.com/yatalley use api

http://twitter.com/nprnews/haiti-earthquake

#http://twitter.com/RAMhaiti use api
"""

''' crawl through twitter searches'''
class StreamWatcherListener(tweepy.StreamListener):
    
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print self.status_wrapper.fill(status.text)
            print '\n %s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source)
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        print 'Snoozing Zzzzzz'


api = twitter.Api()
email = "haiti.dev10@gmail.com"
api._username = u'haiti_dev'
api._password = u'qygx6nis'
api.PostUpdate("Haiti Dev in progress")
    

def main():
    username = api._username
    password = api._password
    stream = tweepy.Stream(username, password, StreamWatcherListener(), timeout=None)

    # Prompt for mode of streaming
    valid_modes = ['sample', 'filter']
    while True:
        mode = raw_input('Mode? [sample/filter] ')
        if mode in valid_modes:
            break
        print 'Invalid mode! Try again.'

    if mode == 'sample':
        stream.sample()

    elif mode == 'filter':
        follow_list = raw_input('Users to follow (comma separated): ').strip()
        track_list = raw_input('Keywords to track (comma seperated): ').strip()
        if follow_list:
            follow_list = [u for u in follow_list.split(',')]
        else:
            follow_list = None
        if track_list:
            track_list = [k for k in track_list.split(',')]
        else:
            track_list = None

        stream.filter(follow_list, track_list)

# To see this work, please uncomment what you see below

#if __name__ == '__main__':
#    try:
#        main()
#    except KeyboardInterrupt:
#        print '\nGoodbye!'


