# Exercício 05 - Escreva um algoritmo para ler o salário mensal atual de um funcionário
# e o percnetual de reajuste. Calcular  e escrever o vlaor do novo salário

print ('Calculo de reajuste salarial ')
salario_atual = float(input('Qual o seu salário atual\n'))
percentual_reajuste = float(input('Qual o percentual de reajuste\n'))

valor_aumento = salario_atual * percentual_reajuste / 100
novo_salario = salario_atual + valor_aumento

print ('Salario Atual: {}  => Novo Salario: {}'.format(salario_atual, novo_salario))


