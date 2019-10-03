
# programa principal 

#importa a framework Flask
from flask import Flask, render_template, request, redirect
from models.cerveja import cerveja

#iniciliza a framework Flask
app=Flask(__name__)

lista_cervejas = []

#direciona a rota, defina a função
@app.route('/')
def inc():
    return render_template('tbl.html', titulo_pagina = 'Home')

#direciona a rota, defina a função
@app.route('/listar')
def listar():
    return render_template('listar.html',  titulo_pagina = 'Listar', lista = lista_cervejas)

#direciona a rota, defina a função
@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html',  titulo_pagina = 'Cadastrar')

#direciona a rota, defina a função
@app.route('/fazer_pedido', methods = ['POST'])
def fazerpedido():
    nome  = request.form['nome']
    return render_template('fazer_pedido.html',  titulo_pagina = 'Pedido')

 #direciona a rota, defina a função
@app.route('/salvar', methods=['POST'])
def salvar(): 
    nome  = request.form['nome']
    tipo  = request.form['tipo']
    preco  = request.form['preco']
    validade  = request.form['validade']
    nova_cerveja = cerveja(nome, tipo, preco, validade)
    lista_cervejas.append(nova_cerveja)
    return redirect('/listar')
app.run()