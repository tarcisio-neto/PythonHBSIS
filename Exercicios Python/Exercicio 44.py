# 43- 44- Ler um valor inteiro (aceitar somente valores entre 1 e 10)
#  e escrever a tabuada de 1 a 10 do valor lido.


print ('Tabuada')
print ('digite o número que vc quer lista a tabuada: ')
num = int(input())

while num == 0 or num > 10:
    print ('Numero invalido!!!\n O número deve ser entre 1 e 10\n Digite outro valor!')
    num = int(input())
    
for multiplicador in range(1,11,1):
    resultado = num * multiplicador
    print('{} x {} = {}'.format(num,multiplicador,resultado))
