# Exercício 03 - Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias
#                e escreva a idade dessa pessoa expressa apenas em dias.
#                 Considerar ano  com 365 dias e mês com  30 dias

print ('Digite sua idade em anos ')
idade_anos = int(input())

print ('Digite a idade em meses: ')
idade_meses = int(input())

print ('Digite a idade em dias: ')
idade_dias = int(input())

resultado_dias = (idade_anos * 365) + (idade_meses * 30) + (idade_dias)

print ('Sua idade em dias é  {}'.format(resultado_dias))