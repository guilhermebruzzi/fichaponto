#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from flask import Flask, redirect, url_for, session, request, abort, make_response
from config import get_app, project_root
from helpers import render_template
from controllers import get_or_create_user
from gmail import send_email


app = get_app() #  Explicitando uma variável app nesse arquivo para o Heroku achar

def __make_response_plain_text__(response_text):
    response = make_response(response_text)
    response.headers["Content-type"] = "text/plain"
    return response

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    return __make_response_plain_text__(open('%s/fichaponto/static/sitemap.xml' % project_root).read())


@app.route('/robots.txt', methods=['GET'])
def robots():
    return __make_response_plain_text__(open('%s/fichaponto/static/robots.txt' % project_root).read())

@app.route('/', methods=['GET', 'POST'])
def index():
    user = None
    if request.method == 'POST':
        user = get_or_create_user(empresa=request.form['empresa'], email=request.form['email'])
        if user:
            src_root = os.path.abspath(os.path.dirname(__file__))
            file_path = os.path.abspath("%s/static/img/exemplo-fichaponto.jpg" % src_root)
            body = """
            <p>
                Mande o seu primeiro email para ficha.ponto.contato@gmail.com falando em cada linha:<br>
                a área de tarefa - descrição única da tarefa - quantidade de horas gastas.
            </p>
            <p>
                Veja um exemplo em anexo do usuário guilherme.bruzzi da empresa ejcm (domínio ejcm.com.br).
            </p>
            """
            send_email(to=[user.email], subject="Bem vindo ao Ficha Ponto", body=body, file_path=file_path)

    return render_template("index.html", user=user)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
