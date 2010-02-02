import json
j = open('geotagged_tweets_from_haiti.json')
from pprint import pprint
for i in j.readlines():
    print i
