# Escreva um algoritmo para ler o número total de eleitores de um município, 
# o número de votos brancos, nulos e válidos. Calcular e escrever o 
# percentual que cada um representa em relação ao total de eleitores.

print("Calculo de saldo de eleição")
print('Qual o numero de eleitores:::')
eleitores = int(input())
print('Qual o numero de votos brancos:::')
brancos = int(input())
print('Qual o numero de votos nulos:::')
nulos = int(input())
print('Qual o numero de votos validos:::')
validos = int(input())

perc_brancos = brancos / eleitores * 100
perc_nulos = nulos / eleitores * 100
perc_validos = validos / eleitores * 100

print('% Brancos: {:.2f}\n% Nulos: {:.2f}\n% Validos: {:.2f}'
    .format(perc_brancos, perc_nulos, perc_validos))