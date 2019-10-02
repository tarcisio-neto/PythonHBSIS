# 34- Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO,
#  deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor
#  zero e imprimir o resultado da divisão do primeiro valor lido pelo segundo valor lido.
# (utilizar a estrutura WHILE).

#5- Acrescentar uma mensagem de 'VALOR INVÁLIDO' no exercício anterior caso o 
# segundo valor informado seja ZERO.

print ('Digite o número 01:  ')
numero_01 = int(input())

print ('Digite o número 02:  ')
numero_02 = int(input())

while numero_02 == 0:
    print('Valor Inválido!!\nO Numero 02 não pode ser zero, informe outro valor')
    numero_02 = int(input())

resultado = numero_01 / numero_02
print(' Número 01 / Número 02 = {:.2f}'.format(resultado))

