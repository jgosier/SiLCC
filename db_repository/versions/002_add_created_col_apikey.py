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
    Column('comment', VARCHAR(256))                                                                     
)                                                                                                                    


def upgrade():
    sql = "ALTER TABLE apikey ADD COLUMN created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;"
    migrate_engine.execute(sql);


def downgrade():
    sql = "ALTER TABLE apikey DROP created;"
    migrate_engine.execute(sql);
    
