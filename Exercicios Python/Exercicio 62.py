# 62- Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 
# 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.


print('Leitor de Vetor')

vetor = []

for i in range(0,5):
    print('Digite a {}ª posição do vetor: '.format(i+1))
    vetor.append(int(input()))
print('A ordem inversa é :', end='')
for i in range(len(vetor)-1,-1, -1):
    print('{},'.format(vetor[i]), end='')












