import logging
import datetime

import simplejson

from pylons import request, response, session, tmpl_context as c, url, config
from pylons.controllers.util import abort, redirect

from sqlalchemy import and_, desc, func, or_, select

from silcc.lib.base import BaseController, render
from silcc.lib.tweettagger import TweetTagger
from silcc.lib.util import get_host
from silcc.model import APIKey, APICall
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
        ip_address = request.environ.get("X_FORWARDED_FOR",
                                         request.environ.get("HTTP_X_FORWARDED_FOR",
                                                             request.environ.get("REMOTE_ADDR")))

        log.info('apikey=%s referrer=%s host=%s', apikey, referrer, host)

        allow_keyless_calls = config.get('allow_keyless_calls') and \
            config.get('allow_keyless_calls').lower() == 'true'

        if not apikey and not allow_keyless_calls:
            # From Swift River API docs:
            # 007 Access denied. Your API key is no longer valid.  Please contact the administrator.
            # 008 Access denied. You need an API key to perform that task.  Please contact the administrator.
            response.status = '401 Unauthorized'
            return "008 Access denied. You need an API key to perform that task. Please contact the administrator."
        
        if apikey:
            # Now load the key from the db if it exists...
            key = Session.query(APIKey).filter_by(keystr=apikey).first()
            if not key:
                log.info('No matching key was found in the db.')
                response.status = '401 Unauthorized'
                return "008 Access denied. You need an API key to perform that task.  Please contact the administrator."

        # Check that the key is valid for the referrer host...
        if apikey and key and (key.valid_domains != host and key.valid_domains != '*'):
            log.info("A Key was found but the referring host is invalid.")
            response.status = '401 Unauthorized'
            return "008 Access denied. You need an API key to perform that task.  Please contact the administrator."
            
        # Now check the number of calls in the last minute...
        query = select([func.count(APICall.table.c.id)])
        query = query.where("called_at > now() - interval 1 minute") 
        if apikey and key:
            # Note that if apikey was supplied and it doesnt exist we would have exited earlier...
            query = query.where(APICall.table.c.apikey_id==key.id)
        else:
            query = query.where(APICall.table.c.called_from==ip_address)
        results = Session.execute(query).fetchone()
        log.info('number of previous calls: %s', str(results))

        prev_calls = results[0]
        if not apikey and prev_calls >= 60: 
            # Keyless calls allow max of 60 per minute per ip address
            log.info("Over throttle limit for keyless calls from ip %s.", ip_address)
            response.status = '401 Unauthorized'
            return "008 Access denied. You have exceeded the maximum allowed calls. Please try again later"
        
        if apikey and key:
            if prev_calls >= key.calls_per_minute:
                log.info("Over throttle limit for key %s.", key.id)
                response.status = '401 Unauthorized'
                return "008 Access denied. You have exceeded the maximum allowed calls. Please try again later"

        # The text parameter is required for the tag method
        if not text:
            log.info('Missing text parameter.')
            return "001 Missing Parameter: Required parameter is not supplied (text)."

        log.info('Text to be tagged: %s', text)
        tags = TweetTagger.tag(text)
        log.info('Tags extracted: %s', str(tags))

        # Now update the call count on the key row...
        if apikey and key:
            key.calls = key.calls + 1
            key.last_call = datetime.datetime.now()

        # Log the api call
        apicall = APICall()
        apicall.parameters = text
        apicall.result = simplejson.dumps(tags)
        if apikey and key:
            apicall.apikey_id = key.id
        apicall.method = 'tag'
        apicall.http_method = request.method
        apicall.called_from = ip_address
        Session.add(apicall)

        Session.commit()
        response.headers['Content-Type'] = 'application/json'
        return simplejson.dumps(tags)

