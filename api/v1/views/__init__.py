#!/usr/bin/python3
"""" Initializes files """
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefixes="/api/v1")

from api.v1.views.index import *
