# - - Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga 
# se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).


print ('Digite ano atual ')
ano_atual = int(input())

print ('Digite ano nascimento ')
ano_nascimento = int(input())

idade = (ano_atual-ano_nascimento)

if idade >= 16:
    print('Pode votar')
else:
    print('Não pode votar')

