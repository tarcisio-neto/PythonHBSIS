lista = ['aluno', 'nota', 'matricula']

arquivo = open('provinha.txt', 'w')
for l in lista:
    arquivo.write('{} \n'.format(l))
arquivo.close()

arquivo = open('provinha.txt', 'r')

for i in arquivo:
    print(i.strip())