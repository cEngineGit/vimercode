#!/usr/bin/python
# -*- coding: utf-8 -*-

import setting

from bottle import debug, run
from bottle import TEMPLATE_PATH

from web.index import app

if __name__ == '__main__':
    debug(True)
    run(app, host="0.0.0.0", port=80, reloader=True)