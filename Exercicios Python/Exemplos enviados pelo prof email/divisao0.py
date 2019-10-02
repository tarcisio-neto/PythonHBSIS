print('digite o valor de n1')
n1 = int(input())
print('digite o valor de n2')
n2 = int(input())

while n2 == 0:
    print('n2 não pode ser zero, forneça um novo valor')
    n2 = int(input())

resultado = n1 / n2
print('n1 / n2 = {}'.format(resultado))



print('digite o valor de n1')
n1 = int(input())
n2 = 0
while n2 == 0:
    print('digite o valor de n2')
    n2 = int(input())
    if n2 == 0:
        print('valor invalido, n2 n pode ser 0')
resultado = n1 / n2
print('n1 / n2 = {}'.format(resultado))