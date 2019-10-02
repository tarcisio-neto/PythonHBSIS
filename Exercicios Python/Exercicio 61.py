# 61- Ler um vetor A de 10 números. Após, ler mais um número e guardar em uma variável X. 
# Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X.
#  Logo após, imprimir o vetor M.



print('Leitor de Vetor')

vetor_A = []

for i in range(0,10):
    print('Digite a {}ª posição do vetor: '.format(i+1))
    vetor_A.append(int(input()))

print('Digite um numero multiplicador: ')
x=int(input())

vetor_B = []

for i in range(0,10):
    vetor_B.append(vetor_A[i]*x)
    print(vetor_B[i],', ', end='')












