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
    Column('valid_from', DATETIME, default=datetime.datetime.now()),
    Column('valid_to', DATETIME, server_default='2020-01-01'),                 
    Column('comment', VARCHAR(256)),
    Column('created', TIMESTAMP)
)                                                                                                                    

# New Columns
calls_per_minute_col = Column('calls_per_minute', INTEGER, server_default='60')

def upgrade():
    sql = "alter table apikey add calls_per_minute integer default 60"
    migrate_engine.execute(sql);


def downgrade():
    sql = "alter table apikey drop calls_per_minute"
    migrate_engine.execute(sql);
