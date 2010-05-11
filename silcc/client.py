"""Python Bindings for SiLCC tagging API"""
import urllib2
import urllib

import simplejson

def tag(text):
    """Calls the SilCC web service API"""
    if type(text) == unicode:
        text = text.encode('utf-8')
    values = dict(text=text, key='AAAABBBB')
    data = urllib.urlencode(values)
    request = urllib2.Request('http://opensilcc.com/api/tag', data)
    json_response = urllib2.urlopen(request)
    json_data = json_response.read()
    json_response.close()
    retval = simplejson.loads(json_data)
    return retval

if __name__ == '__main__':
    tags = tag("Ushahidi is a platform for tracking crisis data")
    print tags

