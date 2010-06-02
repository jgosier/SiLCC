import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# Existing tables
example_table = Table('example', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('apicall_id', Integer, ForeignKey('apicall.id')),
    Column('text', mysql.MSMediumText, nullable=False),
    Column('tags', mysql.MSMediumText, nullable=False),
    Column('corpus', VARCHAR(32), nullable=False)
)                                                                                                                    

def upgrade():
    sql = "ALTER TABLE example ADD COLUMN created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;"
    migrate_engine.execute(sql);


def downgrade():
    sql = "ALTER TABLE example DROP created;"
    migrate_engine.execute(sql);
    
