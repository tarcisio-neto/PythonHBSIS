# Criar um algoritmo para simular o cadastro de itens em um estoque

print('Bem vindo ao controle de estoque')

print('Inserir um novo item::: S - Sim, N - Não')
inserir_item = input()

itens_nome = []
itens_preco = []
while(inserir_item == 'S'):
    print('Nome do item:::')
    nome = input()
    print('Preço do item:::')
    preco = float(input())

    itens_nome.append(nome)
    itens_preco.append(preco)

    print('Inserir um novo item::: S - Sim, N - Não')
    inserir_item = input()

print('Estoque Atual')
print('Produto | Preço')
for i in range(0, len(itens_nome)):
    nome = itens_nome[i]
    preco = itens_preco[i]
    print('{} | {}'.format(nome, preco))