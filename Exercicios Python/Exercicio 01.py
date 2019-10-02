# -Exercicio 01 Escreva um lagoritmo para ler um valor e escrever na tela o seu antecessor.
print('Digite um numero :')
valor = int(input())

valor_antes = valor -1
print ('O Antecessor do {} é {}'.format(valor,valor_antes))
#outra opção
print ('O Antecessor de ' , valor , 'é' , valor_antes)