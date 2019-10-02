# 49- Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior
#  a 40 devem ser somados. Escreva o valor final da soma efetuada.


soma_num = 0

for contador in range(0,10,1):
    print('digite o {}º número'.format(contador + 1))
    num = int(input())
    if num < 40:
        soma_num = soma_num + num
print('A soma dos valores menores que 40 é {}'.format(soma_num))
