# 20- Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
#  calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito).
#  Também testar se saldo atual for maior ou igual a zero escrever a mensagem
#  'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

print ('Digite número da conta:  ')
numero_conta = int(input())

print ('Digite saldo da conta: ')
saldo_conta = float(input())

print ('Digite valor débitado: ')
valor_debitado = float(input())

print ('Digite valor de depósito: ')
valor_deposito = float(input())

saldo_atual = float(saldo_conta + valor_deposito) - valor_debitado

print('O saldo atual da conta é {:.2f}'.format(saldo_atual))
if saldo_atual >= 0:
    print('Seu saldo é Positivo')
else:
    print('Seu saldo é Negativo')    

