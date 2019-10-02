# 43- Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).


print ('Escreva a tabuada do numero 8')

num = 8

while num == 0:
    num = int(input())
    
for multiplicador in range(1,11,1):
    resultado = num * multiplicador
    print('{} x {} = {}'.format(num,multiplicador,resultado))
