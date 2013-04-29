# -*- coding: utf-8 -*-

import os
import sys

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

def add_path():
    global project_root
    file_path = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.abspath("%s/../" % file_path)
    sys.path.insert(0, project_root)
    return project_root

project_root = add_path()

def import_folder(folder_name, base_path = None):
    full_path = os.path.join(base_path, folder_name)
    folder = os.path.abspath(full_path)
    sys.path.insert(0, folder)


import_folder(folder_name='fichaponto', base_path=project_root)

app = Flask(__name__)
app.config.from_pyfile('app.cfg')

# Converte de variaveis de ambiente para config do flask

if "DATABASE_URL" in os.environ:
    os.environ["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]

# Esse for converte qualquer tipo de variavel
for key in app.config.keys():
    if os.environ.has_key(key):
        type_of_config = type(app.config[key])
        if type_of_config is bool:
            if os.environ[key] == "False":
                app.config[key] = False
            else:
                app.config[key] = True
        elif type_of_config is int:
            app.config[key] = int(os.environ[key])
        else:
            app.config[key] = os.environ[key]

# Config do sqlalchemy (mysql)
db = SQLAlchemy(app)

def get_app():
    return app

