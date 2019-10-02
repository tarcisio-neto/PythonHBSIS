# Exercício 06 - - O custo de um carro novo ao consumidor é a soma do custo de fábrica com a 
# porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo
#  que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo
#  para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.




print ('Calculo valor Carro ')
valor_fabrica = float(input("Qual valor de fabrica?\n"))
percentual_distribuidor = float(valor_fabrica * 0.28)
Impostos = float(valor_fabrica * 0.45)
preco_consumidor = (valor_fabrica + percentual_distribuidor + Impostos)

print( 'O valor final para o cosumidor é de {} '.format(preco_consumidor))


