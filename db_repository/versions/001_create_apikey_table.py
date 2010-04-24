import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# New tables
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
    Column('last_call', DATETIME)                 
    # Note: SQLAlchemy doesnt seem to have a way to create a current_timestamp col
    # So see upgrade script 2 where we do it with raw sql.
    #Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    
                                                                                                                    


def upgrade():
    apikey_table.create()

def downgrade():
    apikey_table.drop()

