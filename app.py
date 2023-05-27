#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Hackathon IDP

Equipe: João Vitor Brandão, Rafael Nogueira, Lucas Rocha, João Victor Távora

'''

import flask
from flask import Flask, render_template, request, redirect, session

import requests

import pandas as pd

'''
from analise import get_data
from analise2 import get_data2
from analise3 import get_data3

data = get_data()
print(data)

data2=get_data2
print(data2)

data3=get_data3
print(data3)

netflix_data=pd.read_csv("static/archive/netflix_titles.csv")
netflix_data.head()

cientist_data=pd.read_csv("static/archive/ds_salaries.csv")
cientist_data.head()
'''


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index_inicial.html')

@app.route("/cardapio")
def cardapio():
    name = request.args.get("name")
    url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
    caminho = '/api/cliente/categorias'
    r = requests.get(url+caminho)
    
    resposta = r.json()
    print(resposta)
    if request.method == 'POST':
         return render_template('cardapio.html',name=name,resposta=resposta,categoria_post=request.form['categoria'])
    return render_template('cardapio.html',name=name,resposta=resposta)

@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.args.get("name")
    url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
    caminho = '/api/cliente/usuarios'
    r = requests.get(url+caminho)
    resposta = r.json()
    
    name = request.form['username']
    passw = request.form['password']
    try:
        data = User.query.filter_by(username=name, password=passw).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return 'Erro login - usuário não encontrado'
    except:
        return "Erro Login"

@app.route("/gosto")
def gosto():
    return render_template('gosto.html',data=data,cientist_data=cientist_data,netflix_data=netflix_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)