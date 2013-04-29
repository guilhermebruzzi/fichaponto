#-*- coding:utf-8 -*-

import flask
from config import get_app

app = get_app()

def render_template(url, **data):
    if not "debug" in data.keys():
        data["debug"] = app.config["DEBUG"]

    return flask.render_template(url, **data)
