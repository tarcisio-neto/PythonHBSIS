# 63- Faça um algoritmo para ler um valor N qualquer (que será o tamanho dos vetores). 
# Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor
#  Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições)
#  e escrever o vetor Soma.


print('Leitor de Vetor')

vetor = []

for i in range(0,5):
    print('Digite a {}ª posição do vetor: '.format(i+1))
    vetor.append(int(input()))
print('A ordem inversa é :', end='')
for i in range(len(vetor)-1,-1, -1):
    print('{},'.format(vetor[i]), end='')












