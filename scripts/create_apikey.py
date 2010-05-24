"""Generates API Keys and stores them in the db"""
import sys
import random
from optparse import OptionParser # command-line option parser                                                                                                  

from paste.deploy import appconfig
from pylons import app_globals
from sqlalchemy import select, and_, create_engine, MetaData

from silcc.config.environment import load_environment
from silcc.model.meta import Session
from silcc.model import APIKey

# Valid chars for api keys...
KEYCHARS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--ini',
                      help='INI file to use for application settings',
                      type='str',
                      default='development.ini')
    parser.add_option('--keylength',
                      help='Length in characters of API Key (default 10).',
                      type='int',
                      default=10)
    parser.add_option('--value',
                      help='Use to specify an exact string for the key, if not set it is randomly generated.',
                      type='str',
                      default=None)
    parser.add_option('--owner_name',
                      help='The name (or email address) of the owner of this key.',
                      type="str",
                      default=None)
    parser.add_option('--owner_url',
                      help='Optional url of the owners application that will use the api or owners website.',
                      type='str',
                      default=None)
    parser.add_option('--valid_domains',
                      help='List of comma seperated domains from which the key is valid, default is all (*).',
                      type='str',
                      default='*')
    parser.add_option('--calls_per_minute',
                      help='Number of calls per minute allowed. Default is 60.',
                      type='int',
                      default=60)
    (options, args) = parser.parse_args()

    if not options.owner_name:
        parser.error("You must supply the owner name. (--owner_name).")

    if not options.value:
        random.shuffle(KEYCHARS)
        options.value = ''.join(KEYCHARS[0:options.keylength])

    conf = appconfig('config:' + options.ini, relative_to='.')
    load_environment(conf.global_conf, conf.local_conf)

    engine = create_engine(conf['sqlalchemy.url'], echo=True)
    meta = MetaData()
    conn = engine.connect()

    apikey = APIKey()
    apikey.owner_name = options.owner_name
    apikey.keystr = options.value
    apikey.owner_url = options.owner_url
    apikey.valid_domains = options.valid_domains
    apikey.calls_per_minute = options.calls_per_minute

    Session.add(apikey)
    Session.commit()

    print "Thanks for applying to be an Alpha Tester for Swift Web Services."
    print "Here is your API key for OpenSiLCC: %s" % options.value

