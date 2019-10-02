# - Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever
#  o valor correspondente em graus Celsius (baseado na fórmula abaixo): 
 
# Observação: Para testar se a sua resposta está correta saiba que 100ºC = 212F

print ('qual temperatura em Fahrenheit? ')
temp_fahrenheit = float(input())

temp_celcius = ((temp_fahrenheit -32) *5)/9

print ("A temperatura em Celsius é {:.2f}".format(temp_celcius))

