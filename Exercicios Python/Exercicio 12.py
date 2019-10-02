# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas
#  pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o
#  custo total da compra.



print ('Digite quantidade maças ')
quantidade_macas = int(input())

if quantidade_macas < 12:
    valor_compra = int(quantidade_macas * 1.30)
    print('O valor da compra é de {}'.format(valor_compra))
else:
    valor_compra = int(quantidade_macas *1.0)
    print('O valor da compra é de {}'.format(valor_compra))

