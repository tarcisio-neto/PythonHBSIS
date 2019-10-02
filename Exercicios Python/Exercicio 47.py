# 47- Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos,
#  calcular e escrever a média aritmética dessas notas lidas.

print('Qual a Qtde de alunos da sala? ')
qtde_alunos = int(input())



soma_notas = 0

for contador in range(0,qtde_alunos,1):
    print('digite a nota do {}º aluno'.format(contador + 1))
    nota_aluno = int(input())
    soma_notas = soma_notas + nota_aluno
media = soma_notas /qtde_alunos
        
print('A média aritimética das notas dos {} alunos é {}'.format(qtde_alunos,media))
