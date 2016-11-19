# -*- coding: utf-8 -*-
from flask import Blueprint

melody = Blueprint('melody', import_name=__name__, url_prefix='/melody')

from . import views

