# -*- coding: utf-8 -*-
from flask import render_template, redirect

from . import melody


@melody.route('/')
def home() :
    return render_template('melody/index.html')
