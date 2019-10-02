# 51- O mesmo exercício anterior, mas agora, considere que o segundo valor lido poderá ser maior
#  ou menor que o primeiro valor lido, ou seja, deve-se testá-los.


print('Digite valor 01: ')
valor_01 = int(input())


print('Digite valor 02: ')
valor_02 = int(input())
while valor_02 <= valor_01:
    print('Valor Inválido!! O Segundo valor dever ser maior que o primeiro\n Digite outro valor:  ')
    valor_02 = int(input())

soma = 0
for contador in range(valor_01,valor_02+1,1):
    soma = soma + contador
print('A soma dos valores entre {} e {} é {}'.format(valor_01, valor_02,soma))
