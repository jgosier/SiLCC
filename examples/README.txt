This directory contains a few examples of using the Web API.

twitter_stream.py - Listens to the twitter live stream and
tags incoming tweets in real-time. Uses the Twitter streaming
API in conjunction with the SilCC Web Api.
Run twitter_stream.py  --help to see parameters.


an example run:

$ python examples/twitter_stream.py  --username=myname --password=secret --track=haiti 
1 of 10
Motherless Child- The Orphans of Haiti http://goo.gl/fb/jrwrJ
['Motherless', 'Child', 'Orphans', 'Haiti']
2 of 10
RT @gentilesenat: FYI: there's a tent city 50 meters from the river at Santo ... #haiti
['FYI', 'tent', 'city', 'meters', 'river', 'Santo', 'haiti']
3 of 10
Support Earthquake Relief and Recovery in Haiti - Buy Sell or Donate on Ebay #ebay #haiti http://bit.ly/8tg0iK
['Support', 'Earthquake', 'Relief', 'Recovery', 'Haiti', 'Buy', 'Sell', 'Donate', 'Ebay']
4 of 10
Protesters in Haiti demand President Preval's resignation, accuse him of profiting from quake http://bit.ly/9CUVYq
['Protesters', 'Haiti', 'demand', 'President', 'Prevals', 'resignation', 'accuse', 'quake']
5 of 10
RT @gentilesenat: Now that rain is stronger than ever #Haiti
['rain', 'Haiti']
6 of 10






