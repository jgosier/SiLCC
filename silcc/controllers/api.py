import logging

import simplejson

from pylons import request, response, session, tmpl_context as c, url, config
from pylons.controllers.util import abort, redirect

from sqlalchemy import and_, desc, func, or_, select

from silcc.lib.base import BaseController, render
from silcc.lib.tweettagger import TweetTagger
from silcc.lib.util import get_host
from silcc.model import APIKey
from silcc.model.meta import Session


log = logging.getLogger(__name__)

class ApiController(BaseController):

    def demo(self):
        c.apikey = config.get('demo_api_key')
        return render('/silcc_api_demo.mako')
        
    def tag(self):

        text = request.params.get('text')
        apikey = request.params.get('key')
        language = request.params.get('language')
        channel = request.params.get('channel')
        referrer = request.headers.get('REFERER', '/')
        host = get_host(referrer)
        log.info('apikey=%s referrer=%s host=%s', apikey, referrer, host)

        if not apikey:
            # From Swift River API docs:
            # 007 Access denied. Your API key is no longer valid.  Please contact the administrator.
            # 008 Access denied. You need an API key to perform that task.  Please contact the administrator.
            response.status = '401 Unauthorized'
            return "008 Access denied. You need an API key to perform that task.  Please contact the administrator."
        
        # Now check that the API Key is valid...
        key = Session.query(APIKey).filter_by(keystr=apikey).first()
        if not key:
            log.info('No matching key was found in the db.')
            response.status = '401 Unauthorized'
            return "008 Access denied. You need an API key to perform that task.  Please contact the administrator."

        if key.valid_domains != host and key.valid_domains != '*':
            log.info("A Key was found but the referring host is invalid.")
            response.status = '401 Unauthorized'
            return "008 Access denied. You need an API key to perform that task.  Please contact the administrator."
            
        if not text:
            log.info('Missing text parameter.')
            return "001 Missing Parameter: Required parameter is not supplied (text)."

        log.info('Text to be tagged: %s', text)
        tags = TweetTagger.tag(text)
        log.info('Tags extracted: %s', str(tags))
        return simplejson.dumps(tags)

