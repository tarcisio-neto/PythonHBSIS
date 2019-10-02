# Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
# verificar e escrever se existem números repetidos no vetor VET e em 
# que posições se encontram.

# ler os números
# achar os que repetem
# achar as posições de cada numero que repete

numeros = []
qtd_numeros = 6
for i in range(0, qtd_numeros):
    print('Digite o {}ª número'.format(i+1))
    num = int(input())
    numeros.append(num)

numeros_repetidos = []
for i in range(0, qtd_numeros - 1):
    for j in range(i + 1, qtd_numeros):
        if numeros[i] == numeros[j]:

            nao_existe = True
            for k in range(0, len(numeros_repetidos)):
                if numeros[i] == numeros_repetidos[k]:
                    nao_existe = False
            if nao_existe:
                numeros_repetidos.append(numeros[i])

for i in range(0, len(numeros_repetidos)):
    print("O número {} aparece nas seguintes posições".format(numeros_repetidos[i]))
    for j in range(0, len(numeros)):
        if numeros_repetidos[i] == numeros[j]:
            print(j)