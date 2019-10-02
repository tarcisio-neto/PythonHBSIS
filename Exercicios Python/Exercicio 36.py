# 36- Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um aluno, calcule 
# e imprima a média (simples) desse aluno. Só devem ser aceitos valores válidos durante a 
# leitura (0 a 10) para cada nota.


print ('Digite nota 01:  ')
nota_01 = float(input())


while nota_01 < 0 or nota_01 > 10:
    print('Nota 01 inválida!!\n Digite outra nota')
    nota_01 = float(input())

print ('Digite nota 02:  ')
nota_02 = float(input())


while nota_02 < 0 or nota_02 > 10:
    print('Nota 02 inválida!!\nDigite outra nota')
    nota_02 = float(input())


media = (nota_01 + nota_02)/2
print('Média: {:.2f}'.format(media))

