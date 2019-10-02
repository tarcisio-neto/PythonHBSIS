# 59 - Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir
#  o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor.

#60 - O mesmo exercício anterior, mas agora deve escrever o menor elemento do
#  vetor e a respectiva posição dele nesse vetor.


print('Leitor de Vetor')

vetor = []

for i in range(0,5):
    print('Digite a {}ª posição do vetor: '.format(i+1))
    numero = int(input())
    if numero >= 0:
        vetor.append(numero) 
    else:
        while numero < 0:
            print('Valor tem que ser positivo.\n Digite a  {}ª posicão novamente!'.format(i+1))
            numero = int(input())
        vetor.append(numero)

menor_elemento_vetor = 99999
for i in range(0,5):
    if vetor[i] < menor_elemento_vetor:
        menor_elemento_vetor = vetor[i]
        posicao = i+1

print('O valor do menor elemento é {} e sua posição no vetor é {}'.format(menor_elemento_vetor,posicao))









