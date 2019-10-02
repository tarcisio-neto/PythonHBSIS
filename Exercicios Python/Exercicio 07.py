# - Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
#  mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas.
#  Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas,
#  o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.



print ('qual número de carros vnedidos? ')
num_carros_vendidos = int(input())

print ('Qual valor vendido no mes? ')
valor_vendas_mes = float(input())

print ('Qual Salario Fixo vendedor? ')
salario = float(input())

print ('Qual percentual  de comissão por carro vendido? ')
valor_comissao_carro_vendido = float(input())

salario_final = (salario + (num_carros_vendidos* valor_comissao_carro_vendido)+ (valor_vendas_mes * 0.05))

print ('salario_final: {:.2f}'.format(salario_final))



