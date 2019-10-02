# 56- A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes.
#  Faça um algoritmo para coletar dados sobre o salário e número de filhos de cada habitante
#  e após as leituras, escrever: 
#a)	Média de salário da população 
#b)	Média do número de filhos 
#c)	Maior salário dos habitantes 
#d)	Percentual de pessoas com salário menor que R$ 150,00 
#Obs.: O final da leitura dos dados se dará com a entrada de um “salário negativo”.


salario = 0
maior_salario = 0
soma_valores_salarios = 0
qtd_entrevistados =0
soma_qtd_filhos = 0
soma_salarios_baixos=0
qtd_salarios_baixos = 0

print('Digite salário: ')
salario = float(input())

while salario >= 0:
    soma_valores_salarios = soma_valores_salarios + salario
    qtd_entrevistados = qtd_entrevistados + 1
    if salario > maior_salario:
        maior_salario = salario
    print('Quantidade de filhos:')
    qtd_filhos = int(input())
    soma_qtd_filhos = soma_qtd_filhos + qtd_filhos
    if salario < 150:
        soma_salarios_baixos = soma_salarios_baixos + salario
        qtd_salarios_baixos = qtd_salarios_baixos + 1
    print('Desaja um novo salário?\n Para sair digite salário negativo:  ')
    salario = float(input())

media_salario_populacao = soma_valores_salarios/qtd_entrevistados
print('A média salarial da população é de {:.2f}'.format(media_salario_populacao))
media_filhos = soma_qtd_filhos/qtd_entrevistados
print('A média de filhos da população é de {:.2f}'.format(media_filhos))
print('O maior salário é de {:.2f}'.format(maior_salario))
percentual_habitantes_salario_baixo = (qtd_salarios_baixos*100)/qtd_entrevistados
print('O percentual de habitantes com salário abaixo de 150,00 é de {}%'.format(percentual_habitantes_salario_baixo))


 