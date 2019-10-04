from flask import Flask, render_template, request, redirect


app=Flask(__name__)

lista_investimentos = []

@app.route('/')
def inc():
    return render_template('index.html', titulo_pagina = 'Home')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar_investimento.html',  titulo_pagina = 'Cadastrar')  

@app.route('/listar')
def listar():
    return render_template('listar.html',  titulo_pagina = 'Listar', lista = lista_investimentos)

@app.route('/salvar', methods=['POST'])
def salvar(): 
    categoria  = request.form['categoria']
    tipo  = request.form['tipo']
    aporte  = request.form['aporte']
    rentabilidade  = request.form['rentabilidade']
    periodo  = request.form['periodo']
    novo_investimento = Investimento(categoria, tipo, aporte, rentabilidade, periodo)
    lista_investimentos.append(novo_investimento)
    return redirect('/listar')  


class Investimento:
    def __init__(self, categoria, tipo, aporte, rentabilidade, periodo_rentabilidade):
        self.categoria = categoria
        self.tipo = tipo
        self.aporte = aporte
        self.rentabilidade = rentabilidade
        self.periodo_rentabilidade = periodo_rentabilidade





#class Carteira_Investimento:
 #   def __init__(self, investimento,quantidade,rentabilidade_mensal, rentabilidade_anual)
 #   self.investimento = Investimento
 #   self.quantidade = quantidade
 #   self.rentabilidade_mensal = rentabilidade_mensal
 #   self.rentabilidade_anual = rentabilidade_anual

app.run()

    
