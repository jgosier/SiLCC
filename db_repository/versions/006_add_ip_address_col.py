import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# Existing tables
apicall_table = Table('apicall', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('apikey_id', Integer, ForeignKey('apikey.id')),
    Column('method', CHAR(20), nullable=False),
    Column('http_method', CHAR(4), nullable=False),               
    Column('parameters', VARCHAR(1024), nullable=False),
    Column('result', VARCHAR(1024)),
    Column('called_at', TIMESTAMP)                  
)                                                                                                                    

def upgrade():
    sql = "ALTER TABLE apicall ADD COLUMN called_from VARCHAR(32);"
    migrate_engine.execute(sql);


def downgrade():
    sql = "ALTER TABLE apicall DROP called_from;"
    migrate_engine.execute(sql);
