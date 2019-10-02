# 41- Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive)
#  e N (inclusive). Considere que o N será sempre maior que ZERO.


print ('contador números')
print ('digite um número:')
num =  int(input())

while num == 0:
    num = int(input())
    
#for contador in range(1,num +1,1):
 #   print(contador)
contador = 0
while contador < num:
    contador = contador +1
    print (contador)