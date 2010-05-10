import sys
import urllib
import urllib2
import base64
import simplejson

from optparse import OptionParser # command-line option parser                                                                                                  

from silcc.client import tag

def connect(feed="http://stream.twitter.com/1/statuses/filter.json", track='apple', username=None, password=None, max=5, encoding='utf-8'):
    values = dict(track=track)
    data = urllib.urlencode(values)
    request = urllib2.Request(feed, data)
    base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
    request.add_header("Authorization", "Basic %s" % base64string)
    s = urllib2.urlopen(request)
    count = 0
    for line in iter(s.readline, None):
        count += 1
        print '%s of %s' % (count, max)
        try:
            tweet = simplejson.loads(line)
        except:
            print 'JSON load failed on line===>%s ' % line
            continue
        text = tweet.get('text')
        print text.encode(encoding, 'replace')
        tags = tag(text)
        print tags
        if count >= max:
            break


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--username',
                      help='Twitter username.',
                      type='str',
                      default=None)
    parser.add_option('--password',
                      help='Twitter password',
                      type='str',
                      default=None)
    parser.add_option('--max',
                      help='Max tweets to grab',
                      type="int",
                      default=10)
    parser.add_option('--track',
                      help='The search term/keyword to track e.g. earthquake',
                      type='str',
                      default='earthquake')
    parser.add_option('--encoding',
                      help='Character encoding to use when printing, default is utf-8',
                      type='str',
                      default='utf-8')
    (options, args) = parser.parse_args()

    connect(username=options.username, password=options.password, max=options.max, 
            track=options.track,
            encoding=options.encoding)
