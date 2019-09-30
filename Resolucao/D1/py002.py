#Criar um programa que utilize o método 50-20-10-20: (PaginaSobreMetodos)
# 1. Leia o salário líquido informado pelo usuário.
# 2. Organize os valores de acordo com o método citado.
# 3. Informe ao usuário qual o valor que ele deve destinar para cada categoria.


print ('='*60)

salario = float(input('{}Digite o salário líquido: '.format(' '*5)))

#imprimir 

print('{}O salário líquido é:{} R${:.2f}'.format(' '*5,'.'*10, salario))

print('{}Gastos básicos:{} R${:.2f}'.format(' '*5,'.'*15, salario*0.5))

print('{}Investimentos LP:{} R${:.2f}'.format(' '*5,'.'*13, salario*0.2))

print('{}Investimentos CP:{} R${:.2f}'.format(' '*5,'.'*13, salario*0.1))

print('{}Livre:{} R${:.2f}'.format(' '*5,'.'*24, salario*0.1))


print ('='*60)

