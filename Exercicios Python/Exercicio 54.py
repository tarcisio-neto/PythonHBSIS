# 54- O mesmo exercício anterior, mas agora não será informado o número de mercadorias em estoque.
#  Então o funcionamento deverá ser da seguinte forma: ler o valor da mercadoria e perguntar
#  ‘MAIS MERCADORIAS (S/N)?’. Ao final, imprimir o valor total em estoque e a média de valor
#  das mercadorias em estoque.

print('Levantamento de estoque')
print('Deseja informar alguma mercadoria (S<>N): ')

opcao_registro_mercadorias = (input())

soma_valores_mercadorias=0
qtd_mercadorias = 0

while opcao_registro_mercadorias =='S' or opcao_registro_mercadorias == 's':
    print('Digite valor da {}ª mercadoria: '.format(qtd_mercadorias+1))
    valor_mercadoria = float(input())
    soma_valores_mercadorias = soma_valores_mercadorias + valor_mercadoria
    qtd_mercadorias = qtd_mercadorias + 1
    print('Deseja informar outra mercadoria (S<>N): ')
    opcao_registro_mercadorias = (input())

media_mercadorias = 0

if qtd_mercadorias > 0:
    media_mercadorias = soma_valores_mercadorias/qtd_mercadorias


print('O valor total em estoque: {}'.format(soma_valores_mercadorias))
print('O valor médio do estoque: {:.2f}'.format(media_mercadorias))
