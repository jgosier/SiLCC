import json
j = open('geotagged_tweets_from_haiti.json')

from pprint import pprint
jsonobjects = [i for i in j]

l = json.loads(jsonobjects[0])
keys = l.keys()
pprint(keys)

