import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

def upgrade():
    sql = "drop index ix_apikey_keystr on apikey"
    migrate_engine.execute(sql);
    sql = "create unique index ix_apikey_keystr on apikey(keystr)"
    migrate_engine.execute(sql);

def downgrade():
    sql = "drop index ix_apikey_keystr on apikey"
    migrate_engine.execute(sql);
    sql = "create index ix_apikey_keystr on apikey(keystr)"
    migrate_engine.execute(sql);
