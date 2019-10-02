from flask import Flask, render_template , request, redirect
from alunos import Alunos 
pagina_nome = 'Lista Alunos'
aluno1 = Alunos('Tarcísio', 'Neto', 47984097103)
aluno2 = Alunos('Lais', 'Hofmann', 67991720833)
aluno3 = Alunos('João', 'Silva', 47954124511)
aluno4 = Alunos('Maria', 'Souza', 47984097403)

lista_alunos = [aluno1,aluno2,aluno3,aluno4]
app = Flask(__name__)
#definição de função
@app.route('/')
def inicio():
    return render_template('index.html', nome=pagina_nome, lista=lista_alunos)

#Definição de função
@app.route('/novo')
def novo():
    return render_template('novo.html')

#definição de função
@app.route('/salvar', methods=["POST"])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form ['telefone']
    aluno_novo = Alunos(nome, sobrenome,telefone) 
    lista_alunos.append(aluno_novo)
    return redirect('/')
app.run()
