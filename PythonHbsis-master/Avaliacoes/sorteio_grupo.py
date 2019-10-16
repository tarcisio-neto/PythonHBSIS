import random

def ler_alunos():
    with open('alunos.txt','r') as arquivo:
        for a in arquivo:
            lista_alunos.append(a.strip())

def busca_nome_aluno(index):
    return lista_alunos[index]            

lista_alunos = []            
lista_sorteados = []
ler_alunos()

for i in range(1,28):
    sorteado =  random.randint(1,27)
    while(lista_sorteados.count(sorteado) > 0):
        sorteado =  random.randint(1,27)
    lista_sorteados.append(sorteado)

print('='*50)
print('\n'*3)

lista_alunos_sorteados=[]
for i in range(0,26,3):
    lista_grupos = [busca_nome_aluno(lista_sorteados[i]-1), busca_nome_aluno(lista_sorteados[i+1]-1), busca_nome_aluno(lista_sorteados[i+2]-1) ]
    lista_alunos_sorteados.append(lista_grupos)
for i in range(0,9):
    print(f' Grupo: {i+1} ')
    for ig in lista_alunos_sorteados[i]:
        print('{} {}'.format(' '*4 , ig))

print('\n'*3)
print('='*50)
    
