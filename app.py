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
        name = request.form['username']
        passw = request.form['password']
        
        url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
        caminho = '/api/cliente/usuarios'
        r = requests.get(url + caminho)
        resposta = r.json()
        
        try:
            # Verifica se o usuário e a senha estão presentes na resposta da API
            if any(u['name'] == name and u['password'] == passw for u in resposta):
                session['logged_in'] = True
                return redirect('index_inicial.html')
            else:
                return 'Erro no login - usuário não encontrado'
        except:
            return 'Erro no login - falha na autenticação'
    
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

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
        caminho = '/api/cliente/usuarios'
        payload = {
            'nome': nome,
            'email': email,
            'senha': senha
        }
        response = requests.post(url + caminho, json=payload)
        
        if response.status_code == 201:
            return 'Cadastro realizado com sucesso!'
        else:
            return 'Erro no cadastro - falha na API'
    
    elif request.method == 'GET':
        return render_template('cadastro.html')





if __name__ == '__main__':
    app.run()