from flask import Flask, render_template, request, redirect
from cliente import Cliente
from categoria import Categoria
from produto import Produto
import MySQLdb

##produto

def listar_produto_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("select * from PRODUTO") 
    listar_produto = []
    for i in cursor.fetchall():
        produto = Produto()
        produto.id = i[0]
        produto.nome = i[1]
        produto.descricao = i[2]
        produto.categoria_id = i[3]
        produto.estoque_id = i[4]
        listar_produto.append(produto)

    conexao.close()
    return listar_produto

##categoria

def salvar_categoria_db(categoria):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO CATEGORIA (TIPO_PRODUTO, DESCRICAO)" + 
    " VALUES ('{}', '{}')".format(categoria.tipo, categoria.descricao))
    conexao.commit()
    conexao.close()

def editar_categoria_db(categoria):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("UPDATE CATEGORIA SET TIPO_PRODUTO = '{}', DESCRICAO = '{}' WHERE ID = {}"
    .format(categoria.tipo, categoria.descricao, categoria.id))
    conexao.commit()
    conexao.close()   

def listar_categoria_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM CATEGORIA")
    lista_categoria = []
    for i in cursor.fetchall():
        categoria = Categoria()
        categoria.id = i[0]
        categoria.tipo = i[1]
        categoria.descricao = i[2]
        lista_categoria.append(categoria)

    conexao.close()
    return lista_categoria

def deletar_categoria(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM CATEGORIA WHERE id={}".format(id))
    conexao.commit()
    conexao.close()

def alterar_categoria_db(categoria):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("UPDATE CATEGORIA SET( tipo_produto='{}', descricao='{}') WHERE id={}"
    .format(categoria.tipo, categoria.descricao, categoria.id))
    conexao.commit()

def buscar_categoria_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM CATEGORIA WHERE id ={}'.format(id))
    c = Categoria()
    for i in cursor.fetchall():
        c.id = i[0]
        c.tipo = i[1]
        c.descricao = i[2]
    conexao.close()
    return c



def listar_clientes():
    cliente1 = Cliente()
    cliente1.id = 1
    cliente1.nome = 'Luisinho'
    cliente1.cpf = '082.730.329-73'
    cliente1.nascimento = '15/04/1998'
    lista = [cliente1]
    return lista

def listar_clientes_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Cliente")
    lista_cliente = []
    for i in cursor.fetchall():
        cliente2 = Cliente()
        cliente2.id = i[0]
        cliente2.nome = i[1]
        cliente2.cpf = i[2]
        cliente2.nascimento = i[3]
        lista_cliente.append(cliente2)
    conexao.close()
    return lista_cliente

def salvar_cliente_db(nome, cpf,dt_nasc):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Cliente (nome,cpf,data_nascimento)" + 
    " VALUES ('{}', '{}', '{}')".format(nome,cpf,dt_nasc))
    conexao.commit()
    conexao.close()

def deletar_cliente(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Cliente WHERE id={}".format(id))
    conexao.commit()
    conexao.close()

def alterar_cliente_db(cliente):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("UPDATE Cliente SET nome='{}', cpf='{}', data_nascimento='{}' WHERE ID={}"
    .format(cliente.nome, cliente.cpf, cliente.nascimento , cliente.id))
    conexao.commit()

def buscar_cliente_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Cliente WHERE id ={}'.format(id))
    c = Cliente()
    for i in cursor.fetchall():
        c.id = i[0]
        c.nome = i[1]
        c.cpf = i[2]
        c.nascimento = i[3]
    conexao.close()
    return c


nome_de_la_page = "Nome da pagina"

app= Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome_de_la_page = nome_de_la_page)

@app.route('/cliente/lista')
def lista_cliente():
    lista = listar_clientes_db()
    return render_template('lista_cliente.html', nome_de_la_page = nome_de_la_page, lista = lista)

@app.route('/cliente')
def cliente():
    return render_template('cliente.html', nome_de_la_page = nome_de_la_page)

@app.route('/cliente/salvar', methods = ['POST'])
def salvar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    nascimento = request.form['nascimento']
    cliente = Cliente()
    cliente.nome = nome 
    cliente.cpf = cpf
    cliente.nascimento = nascimento
    salvar_cliente_db(cliente.nome, cliente.cpf, cliente.nascimento)
    return redirect('/cliente/lista')

@app.route('/cliente/delete')
def deletar():
    id = request.args['id']
    deletar_cliente(id)
    return redirect ('/cliente/lista')

@app.route('/cliente/alterar')
def cliente_alterar():
    id = request.args['id']    
    cliente = buscar_cliente_por_id(id)
    return render_template('cliente_alterar.html', cliente=cliente)

@app.route('/cliente/alterar/salvar', methods=['POST'])
def cliente_alterar_salvar():
    id = request.form['id']
    nome = request.form['nome']
    cpf = request.form['cpf']
    nascimento = request.form['nascimento']
    cliente = Cliente()
    cliente.id = id 
    cliente.nome = nome 
    cliente.cpf = cpf
    cliente.nascimento = nascimento
    alterar_cliente_db(cliente)
    return redirect ('/cliente/lista')

#################### CATEGORIA ###############################

@app.route('/categoria')
def categoria():
    return render_template('categoria.html')

@app.route('/categoria/salvar', methods=['POST'])
def salvar_categoria():
    tipo = request.form['tipo']
    descricao = request.form['descricao']
    categoria = Categoria()
    categoria.tipo = tipo 
    categoria.descricao = descricao
    salvar_categoria_db(categoria)
    return redirect('/categoria/lista')

@app.route('/categoria/lista')
def lista_categoria():
    lista_volta = listar_categoria_db()
    return render_template('lista_categorias.html', lista=lista_volta)

@app.route('/categoria/delete')
def apagar_categoria():
    id = request.args['id']
    deletar_categoria(id)
    return redirect('/categoria/lista')

@app.route('/categoria/alterar')
def alterar_categoria():
    id = request.args['id']    
    categoria = buscar_categoria_por_id(id)
    return render_template('editar_categoria.html', categoria = categoria)

@app.route('/categoria/alterar/salvar', methods=['POST'])
def alterar_categoria_salvar():
    id = request.form['id']
    tipo = request.form['tipo']
    descricao = request.form['descricao']
    categoria = Categoria()
    categoria.id = id 
    categoria.tipo = tipo 
    categoria.descricao = descricao
    editar_categoria_db(categoria)
    return redirect('/categoria/lista')

####################### PRODUTOS ########################

@app.route('/produtos')
def produto():
    return render_template('produto.html')

@app.route('/produto/salvar', methods=['POST'])
def salvar_produto():
    return redirect('/produto/lista')

@app.route('/produto/lista')
def listar_produto():
    lista_volta = listar_produto_db()
    return render_template('lista_produto.html', lista=lista_volta)

@app.route('/produto/delete')
def apagar_produto():
    return redirect('/produto/lista')

@app.route('/produto/alterar')
def editar_produto():
    return render_template('editar_produto.html')

@app.route('/produto/alterar/salvar', methods=['POST'])
def alterar_produto_salvar():
    return redirect('/produto/lista')



app.run()
