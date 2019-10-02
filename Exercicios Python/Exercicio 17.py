# - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

print ('Digite valor 01: ')
valor_01 = int(input())

print ('Digite valor 02: ')
valor_02 = int(input())


if valor_02 == valor_01:
    print ('valores iguais')
else:
    if valor_01 > valor_02:
        print('valor 01 é maior')
    else:
        if valor_01 < valor_02:
            print('valor 02 é maior')
      

