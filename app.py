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
    if request.method == 'POST':
        name = request.args.get("name")
        url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
        caminho = '/api/cliente/usuarios'
        r = requests.get(url+caminho)
        resposta = r.json()
        
        name = request.form['username']
        passw = request.form['password']
        try:
            data = '1'
            if data is not None:
                session['logged_in'] = True
                return redirect('index_inicial.html')
            else:
                return 'Erro login - usuário não encontrado'
        except:
            return "Erro Login"
    elif request.method == 'GET':
        return render_template('login.html')

@app.route("/carrinho")
def carrinho():
    return render_template('carrinho.html')

# Antes das rotas, declare uma lista vazia para o carrinho
carrinho = []

@app.route('/carrinho/add/<int:produto_id>', methods=['GET'])
def adicionar_carrinho(produto_id):
    # Lógica para adicionar o produto ao carrinho
    # Você precisa armazenar as informações do produto no carrinho, como foto e descrição
    # ...

    # Exemplo de armazenamento das informações do produto em um dicionário
    produto = {
        'id': produto_id,
        'fotoUrl': 'caminho/para/foto.jpg',
        'descricao': 'Descrição do produto'
    }

    carrinho.append(produto)  # Adiciona o produto à lista do carrinho

    return redirect('/carrinho')

def dropdown_categories():
    selected_options = request.args.getlist('dropdown')
    # Process the selected options here
    return render_template('cardapio.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)