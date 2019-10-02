# - - Ler 3 valores (considere que não serão informados valores iguais) e escrever em ordem crescente.

print ('Digite valor 01: ')
valor_01 = int(input())

print ('Digite valor 02: ')
valor_02 = int(input())

print ('Digite valor 03: ')
valor_03 = int(input())

primeiro_valor = 0
segundo_valor = 0
terceiro_valor = 0


if valor_01 < valor_02 and valor_01 < valor_03:
    primeiro_valor = valor_01
    if valor_02 < valor_03:
        segundo_valor =  valor_02
        terceiro_valor = valor_03
    else:
        segundo_valor = valor_03
        terceiro_valor = valor_02
if valor_02 < valor_01 and valor_02 < valor_03:
    primeiro_valor =  valor_02
    if valor_01 < valor_03:
        segundo_valor =  valor_01
        terceiro_valor = valor_03
    else:
        segundo_valor = valor_03
        terceiro_valor = valor_01
    
if valor_03 < valor_01 and valor_03 < valor_02:
    primeiro_valor =  valor_03
    if valor_02 < valor_01:
        segundo_valor =  valor_02
        terceiro_valor = valor_01
    else:
        segundo_valor = valor_01
        terceiro_valor = valor_02

print (primeiro_valor, ' , ', segundo_valor, ' , ', terceiro_valor)
