#-*- coding:utf-8 -*-

from models import db, User

def get_or_create_user(empresa, email):
    if empresa.strip() == "" or email.strip() == "":
        return None

    user = User.query.filter_by(empresa=empresa, email=email).first()
    if user:
        return user

    user = User(empresa=empresa, email=email)
    db.session.add(user)
    db.session.commit()

    return user

def get_all_users():
    return User.query.order_by('data_criacao').all()
