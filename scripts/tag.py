"""Creates the Database used by the SilCC Api"""
from optparse import OptionParser # command-line option parser                                                                                                  
from pprint import pprint       

import logging
import traceback
import sys
import time
import re
import csv

import feedparser

from paste.deploy import appconfig
from pylons import app_globals
from silcc.config.environment import load_environment
from silcc.lib.tag import extract_tags 

from sqlalchemy import select, and_, create_engine, MetaData
import sqlalchemy as sa


#log = logging.getLogger(__name__)
# Set up logging
#log = logging.getLogger(__name__)
#log.propagate = False
#ch  = logging.StreamHandler(sys.stdout)
#ch_fmt = logging.Formatter('%(asctime)s %(process)d (%(levelname)s): %(message)s') 
#ch.setFormatter(ch_fmt)
#log.addHandler(ch)

'''
See: http://download.geonames.org/export/dump/
We only want to load places of feature class P 
(for now, perhaps more in future?)
'''

#from sqlalchemy.orm import eagerload

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('--ini',
                      help='INI file to use for application settings',
                      type='str',
                      default='development.ini')
    parser.add_option('--text',
                      help='Text to tag.',
                      type='str',
                      default='Major earthquake in Chile')
    parser.add_option('--url',
                      help='An optional rss url to download and tag. (Set --test_feed to true to use)',
                      type='str',
                      default='http://newsrss.bbc.co.uk/rss/newsonline_world_edition/front_page/rss.xml')
    parser.add_option('--test_feed',
                      help='Set to true to tag headlines from a feed set in --url',
                      action='store_true',
                      default=False)
    (options, args) = parser.parse_args()

    conf = appconfig('config:' + options.ini, relative_to='.')
    load_environment(conf.global_conf, conf.local_conf)

    print options.text
    if options.test_feed:
        d =  feedparser.parse('http://newsrss.bbc.co.uk/rss/newsonline_world_edition/front_page/rss.xml')
        entries = d.get('entries')
        for e in entries:
            title = e.get('title')
            print title
            print extract_tags(title)
            print
    else:

        print extract_tags(options.text)

    #engine = create_engine(conf['sqlalchemy.url'], echo=True)
    #meta = MetaData()
    #conn = engine.connect()
    #print conn
    #places_table = sa.Table('places', meta, autoload=True, autoload_with=engine)
    #fh = open(options.filename)
    #line = fh.readline()
    #while line:
    #    parts = line.split('\t')
    #    name = parts[1]
    #    name_ascii = parts[2]
    #    feature_class = parts[6]
    #    if feature_class == 'P':
    #        insert = places_table.insert().values(name=name, name_ascii=name_ascii)
    #        print insert.compile().params
    #        conn.execute(insert)
    #    line = fh.readline()
    #fh.close()

    #print conn
