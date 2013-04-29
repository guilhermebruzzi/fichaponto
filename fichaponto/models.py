# -*- coding: utf-8 -*-

from config import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    data_criacao = db.Column(db.DateTime())

    def __init__(self, empresa, email):
        self.empresa = empresa
        self.email = email
        self.data_criacao = datetime.datetime.now()

    def __eq__(self, other):
        return self.email == other.email and self.empresa == other.empresa

    def __unicode__(self):
        return '%s - %s' % (self.email, self.empresa)
