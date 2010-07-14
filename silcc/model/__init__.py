"""The application's model objects"""
from silcc.model.meta import Session, Base

import sqlalchemy as sa
from sqlalchemy import orm

from silcc.model import meta
from silcc.model.apicall import APICall
from silcc.model.apikey import APIKey
from silcc.model.country import Country
#from silcc.model.place import Place
from silcc.model.example import Example

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

    apikey_table = sa.Table('apikey', meta.metadata, autoload=True, autoload_with=engine)
    APIKey.table = apikey_table
    orm.mapper(APIKey, APIKey.table)

    apicall_table = sa.Table('apicall', meta.metadata, autoload=True, autoload_with=engine)
    APICall.table = apicall_table
    orm.mapper(APICall, APICall.table)
    
    example_table = sa.Table('example', meta.metadata, autoload=True, autoload_with=engine)
    Example.table = example_table
    orm.mapper(Example, Example.table)

    country_table = sa.Table('countries', meta.metadata, autoload=True, autoload_with=engine)
    Country.table = country_table
    orm.mapper(Country, Country.table)
