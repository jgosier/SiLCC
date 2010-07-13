from sqlalchemy import *
from migrate import *
from sqlalchemy.databases import mysql
metadata = MetaData(migrate_engine)

# New tables
acro_table = Table('acronyms', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('name', mysql.MSMediumText, nullable=False),
)   
countries_table = Table('countries', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('name', mysql.MSMediumText, nullable=False),
)   

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    acro_table.create()
    countries_table.create()

def downgrade():
    # Operations to reverse the above upgrade go here.
    acro_table.drop()
    countries_table.drop()

