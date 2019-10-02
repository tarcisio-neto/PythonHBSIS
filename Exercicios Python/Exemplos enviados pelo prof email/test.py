#            0         1        2
# produtos = ['Omo', 'Ariel', 'Brilhante']
# preco    = [   50,      12,  37        ]
# desconto = [    5,       2,   3        ]

# desc = preco[2] * desconto[1] / 100
# print(desc)

# notas_joao = [ 7.0, 5.0, 9.0, 8.0, 7.2, 5.6] # 6
# for i in range(0, len(notas_joao)):
#     print(notas_joao[i])

notas = [
    [ 7.0, 5.0, 9.0], # João
    [ 6.3, 5.0, 8.0], # Maria
    [ 8.0, 8.5, 9.2]  # Ana
]


for i in range(0, len(notas)):
    for j in range(0, len(notas[0])):
        print( '{} '.format( notas[i][j] ), end='' )
    print('')

notas = []
qtd_alunos = int(input('Quantidade de alunos: '))
qtd_notas_aluno = int(input('Quantidade de notas por aluno: '))

for i in range(0, qtd_alunos):
    notas_aluno = []
    notas.append(notas_aluno)
    for j in range(0, qtd_notas_aluno):
        nota = float(input('Digite a {}º nota do aluno {}'.format(j, i)))
        notas_aluno.append(nota)