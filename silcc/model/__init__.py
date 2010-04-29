"""The application's model objects"""
from silcc.model.meta import Session, Base

import sqlalchemy as sa
from sqlalchemy import orm

from silcc.model import meta
from silcc.model.apicall import APICall
from silcc.model.apikey import APIKey
from silcc.model.place import Place

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

    apikey_table = sa.Table('apikey', meta.metadata, autoload=True, autoload_with=engine)
    APIKey.table = apikey_table
    orm.mapper(APIKey, APIKey.table)

    apicall_table = sa.Table('apicall', meta.metadata, autoload=True, autoload_with=engine)
    APICall.table = apicall_table
    orm.mapper(APICall, APICall.table)
    
    #places_table = sa.Table('places', meta.metadata, autoload=True, autoload_with=engine)
    #Place.table = places_table
    #orm.mapper(Place, Place.table)
