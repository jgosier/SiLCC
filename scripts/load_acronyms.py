"""Creates the Database used by the SilCC Api"""
from optparse import OptionParser # command-line option parser                                                                                                  
from pprint import pprint       

import logging
import traceback
import sys
import time
import re
import csv

from paste.deploy import appconfig
from pylons import app_globals
from silcc.config.environment import load_environment
#from silcc.model import tables as t
#from silcc.model.meta import Session

#from silcc.model import meta as meta
#from silcc.model import tables
from sqlalchemy import select, and_, create_engine, MetaData,  Table, Column, Integer, String, ForeignKey
import sqlalchemy as sa

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('--ini',
                      help='INI file to use for application settings',
                      type='str',
                      default='development.ini')
    parser.add_option('--filename',
                      help='File containing place names data.',
                      type='str',
                      default='data/acronyms.txt')
    (options, args) = parser.parse_args()

    conf = appconfig('config:' + options.ini, relative_to='.')
    load_environment(conf.global_conf, conf.local_conf)
    
    engine = create_engine(conf['sqlalchemy.url'], echo=True)
    meta = MetaData()
    conn = engine.connect()

    places_table = sa.Table('acronyms', meta, autoload=True, autoload_with=engine)
    fh = open(options.filename)
    line = fh.readline()
    while line:
	line = line.strip('\n')
        insert = places_table.insert().values(name=line)
        print insert.compile().params
        conn.execute(insert)
        line = fh.readline()
    fh.close()
