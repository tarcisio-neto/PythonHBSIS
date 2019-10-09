class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

def criap(n, sb):
    return {'nome':n, 'sobrenome':sb}

listaDP = []
listaCP = []

n = input('nome: ')
sb = input('sobre: ')
n2 = input('nome: ')
sb2 = input('sobre: ')

listaDP.append( criap(n, sb) )
listaDP.append( criap(n2, sb2) )

listaCP.append( Pessoa(n, sb) )  
listaCP.append( Pessoa(n2, sb2) ) 

for i in range(len(listaDP)):
    p =listaDP[i]
    print( p['nome'] )

for i in range(len(listaCP)):
    pessoa = listaCP[i]
    print('nome: {}, sobrenome {}'.format(pessoa.nome, pessoa.sobrenome)  )

