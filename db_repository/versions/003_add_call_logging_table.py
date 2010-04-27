import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# Existing tables
apikey_table = Table('apikey', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('keystr', CHAR(40), nullable=False, index=True),
    Column('owner_name', VARCHAR(128), nullable=False),
    Column('owner_url', VARCHAR(128)),
    Column('valid_domains', VARCHAR(256)),                 
    Column('valid_from', DATETIME, default=datetime.datetime.now()),
    Column('valid_to', DATETIME, server_default='2020-01-01'),                 
    Column('comment', VARCHAR(256)),
    Column('calls', mysql.MSBigInteger(unsigned=True), server_default='0'),
    Column('last_call', DATETIME),                 
    Column('created', TIMESTAMP)
)                                                                                                                    

# New tables
apicall_table = Table('apicall', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('apikey_id', Integer, ForeignKey('apikey.id')),
    Column('method', CHAR(20), nullable=False),
    Column('http_method', CHAR(4), nullable=False),               
    Column('parameters', VARCHAR(1024), nullable=False),
    Column('result', VARCHAR(1024))
)                                                                                                                    
                                                                                                                    


def upgrade():
    apicall_table.create()

def downgrade():
    apicall_table.drop()
