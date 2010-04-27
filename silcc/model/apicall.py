"""Represents an API Method call (logs calls)"""

import logging
import datetime
import math

from sqlalchemy import and_, desc, func, or_, select, types
from sqlalchemy.sql import text

from silcc.model import meta

log = logging.getLogger(__name__)

class APICall(object):

    pass
