# Exercício 04 - Escreva um algoritmo para ler o número total de eleitores de um município,
#                o número de votos brancos, nulos e válidos. calcular e escrever o 
#                percentual que cada um representa em relação ao total de eleitores.

print ('Calculo de saldo de eleição ')
print ('Qual o numero de eleitores? ')
eleitores = int(input())

print ('Número de votos brancos ')
brancos = int(input())

print ('Número de votos nulos ')
nulos = int(input())

print ('Número de votos válidos ')
validos = int(input())


perc_brancos = brancos / eleitores * 100
perc_nulos = nulos / eleitores * 100
perc_validos = validos / eleitores * 100



print ('% Brancos: {:.2f}\n% Nulos: {:.2f}\n%  Válidos: {:.2f}'
    .format(perc_brancos, perc_nulos, perc_validos))