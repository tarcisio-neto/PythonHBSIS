# 59 - Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir
#  o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor.

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

maior_elemento_vetor = 0
for i in range(0,5):
    if vetor[i] > maior_elemento_vetor:
        maior_elemento_vetor = vetor[i]
        posicao = i+1

print('O valor do maior elemento é {} e sua posição no vetor é {}'.format(maior_elemento_vetor,posicao))









