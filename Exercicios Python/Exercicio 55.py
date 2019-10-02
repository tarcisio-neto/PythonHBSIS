# 55- Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever: 
#•	o maior preço lido.
#•	a média aritmética dos preços dos produtos.

soma_preco_produtos = 0
maior_preco_lido = 0
for qtd_produtos in range(0,3,1):
    print('Digite o código do {}º produto:  '.format(qtd_produtos +1))
    cod_produto = int(input())
    print('Digite o preço do produto:  ')
    preco_produto = float(input())
    soma_preco_produtos = soma_preco_produtos + preco_produto
    if preco_produto > maior_preco_lido:
        maior_preco_lido = preco_produto

media_preco_produtos = soma_preco_produtos /3

print('O Maior preço lido é {:.2f}'.format(maior_preco_lido))
print ('A média dos preços é de {:.2f}'.format(media_preco_produtos))

