# - 19- Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
#  Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais
#  5% sobre o que ultrapassar este valor, calcular e escrever o 
# seu salário total.

print ('Digite Salário Fixo: ')
salario = float(input())

print ('Valor das vendas: ')
valor_vendas = float(input())

comissao_padrao = float(1500 * 0.03)

if valor_vendas <= 1500: 
    salario_total = salario + comissao_padrao
    print ('Salario total é de {}'.format(salario_total))
else:
    comissao_extra = (valor_vendas - 1500) * 0.05
    salario_total = salario + comissao_padrao + comissao_extra
    print ('Salario total é de {}'.format(salario_total))
