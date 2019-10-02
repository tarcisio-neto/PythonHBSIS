# 58- Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos.
#  Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. 
# Escrever a média da turma e o resultado da contagem.

print('Notas da Turma')
notas_alunos = []
soma_notas = 0  
for i in range(0,3):
    print('Digite a {}ª nota: '.format(i+1))
    nota = float(input())
    notas_alunos.append(nota)
    soma_notas = soma_notas + notas_alunos[i]


media_turma = soma_notas / len(notas_alunos)

contador_notas_acima_media = 0
for i in range(0,3):
    if notas_alunos[i] > media_turma:
        contador_notas_acima_media = contador_notas_acima_media + 1

print('A média da turma é {:.2f}'.format(media_turma))
print('Número de notas acima da média é {}'.format(contador_notas_acima_media))





 