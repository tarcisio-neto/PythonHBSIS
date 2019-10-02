# 50- Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2 valores lidos
#  (incluindo os valores lidos na soma). Considere que o segundo valor lido será sempre maior
#  que o primeiro valor lido.


print('Digite valor 01: ')
valor_01 = int(input())


print('Digite valor 02: ')
valor_02 = int(input())
while valor_02 < valor_01:
    print('Valor Inválido!! O Segundo valor dever ser maior que o primeiro\n Digite outro valor:  ')
    valor_02 = int(input())

soma = 0
for contador in range(valor_01,valor_02+1,1):
    soma = soma + contador
print('A soma dos valores entre {} e {} é {}'.format(valor_01, valor_02,soma))
