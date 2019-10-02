# 46- Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.


soma_valores = 0

for valor_atual in range(0,10,1):
    print('digite o {}º'.format(valor_atual + 1))
    num = int(input())
    soma_valores = soma_valores + num
media = soma_valores /10
        
print('A média aritimética dos valores lidos é {}'.format(media))
