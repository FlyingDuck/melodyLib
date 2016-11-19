# -*- coding: utf-8 -*-
from flask import Blueprint

home = Blueprint('home', import_name=__name__, url_prefix='/')

from . import views