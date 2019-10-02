# Fazer uma lista de Patota com 10 atletas  e dar opção para pesquisar quem vai pro jogo.

print('Patota passa bola')

jogadores = []

for i in range(0,4,1):
    print('jogador {}'.format(i + 1))
    jogadores.append(input())

print('Quer pesquisar presença de algum atleta? S - sim  N - não')
deseja_pesquisar_nome = input()

while deseja_pesquisar_nome =='S' or deseja_pesquisar_nome == 's':

    print('Digite o nome que deseja verificar se vai na patota')
    nome = input()
    confirmacao = 'Ausente'
    for i in range(0,4,1):
        if jogadores[i] == nome:
            confirmacao = ('Vai pro jogo!!')
            print('O Atleta {} {}'.format(nome,confirmacao))
    
    if confirmacao == 'Ausente':
        print('Atleta {} {}'.format(nome,confirmacao))

    print('Deseja pesquisar novo atleta? S ou N?')
    deseja_pesquisar_nome = input()
print ('Fim')






