from flask import Flask, render_template, request, redirect

class Pessoa: 
    def __init__(self, nome):
        self.__nome = nome
  
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome



class Aluno(Pessoa):
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        super().__init__(nome)

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

def salvar_aluno(aluno):
    with open('novo.txt','a') as arquivo:
        arquivo.write(f'{aluno.nome},{aluno.cpf} \n')

def listar_aluno():
    lista_aluno = []
    with open('novo.txt','r') as arquivo:
        for i in arquivo:
            aluno_recebido = i.strip().split(',')
            aluno = Aluno(aluno_recebido[1],aluno_recebido[0])
            lista_aluno.append(aluno)
    return lista_aluno

app = Flask(__name__)
pagina_nome = 'lendas'

@app.route ('/')
def prova ():
    return render_template('index.html', pagina_nome = pagina_nome)

@app.route ('/lista')
def lista ():
    return render_template('listalendas.html', pagina_nome = pagina_nome, lista = listar_aluno())   

@app.route ('/cadastro')
def cadastro ():
    return render_template('cadastro.html', pagina_nome = pagina_nome)

@app.route('/salvar-cadastro', methods=['POST'])
def salvar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    aluno = Aluno(cpf, nome)
    salvar_aluno(aluno)
    return redirect('/lista')

app.run()



