# Faça um algoritmo para ler 10 números e armazenar em um vetor. 
# Após isto, o algoritmo deve ordenar os números no vetor em ordem crescente. 
# Escrever o vetor ordenado.

print('Ordenação de listas')

numeros = []
for i in range(0, 5):
    print('Digite o {}º número'.format(i + 1))
    numero = int(input())

    numeros.append(numero)

for i in range(0, 5):
    for j in range(i + 1, 5):
        if numeros[j] < numeros[i]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

for i in range(0, 5):
    print(numeros[i])