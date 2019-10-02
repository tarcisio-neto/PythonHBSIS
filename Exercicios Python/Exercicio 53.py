# 53- Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que 
# permita a entrada das seguintes informações: 
#a)	o número total de mercadorias no estoque; 
#b)	o valor de cada mercadoria. 
#Ao final imprimir o valor total em estoque e a média de valor das mercadorias.


print('Levantamento de estoque')
print('Qual a quantidade  de mercadorias: ')

qtd_mercadorias = int(input())

soma_valores_mercadorias=0

for i in range(0,qtd_mercadorias,1):
    print('Digite valor da {}ª mercadoria: '.format(i+1))
    valor_mercadoria = float(input())
    soma_valores_mercadorias = soma_valores_mercadorias + valor_mercadoria

media = soma_valores_mercadorias/qtd_mercadorias
print('O valor total em estoque: {}'.format(soma_valores_mercadorias))
print('O valor médio do estoque: {:.2f}'.format(media))
