# 48-- Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma
#  total dos 10 números lidos.


soma_num = 0

for contador in range(0,10,1):
    print('digite o {}º número'.format(contador + 1))
    num = int(input())
    soma_num = soma_num + num

        
print('A das notas dos 10 alunos é {}'.format(soma_num))
