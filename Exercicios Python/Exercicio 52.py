# 52- Faça um algoritmo que calcule e escreva a média aritmética dos números inteiros entre
#  15 (inclusive) e 100 (inclusive).

print('Média aritimética')
soma = 0
divisor = 101-15
for contador in range(15,101,1):
    soma = soma + contador
media = (soma /divisor)
print('A média aritimética dos valores entre 15 e 100 é {:.2f}'.format(media))
