"""Represents a named 'Place' (village, city, state, country)"""

import logging
import datetime
import math

from sqlalchemy import and_, desc, func, or_, select, types
from sqlalchemy.sql import text

from silcc.model import meta

log = logging.getLogger(__name__)

class Place(object):

    pass
