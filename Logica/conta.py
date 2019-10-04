num_banco = '12'

def cria_conta(nome, numero_conta, saldo):   
    return {'nome':nome, 'numero_c':numero_conta, 'saldo':saldo }

def depositar(cnt, valor):
    cnt['saldo'] += valor
    
def sacar(cnt,valor):
    cnt['saldo'] -= valor

def mostrarbanco():
    print(num_banco)

mostrarbanco(num_banco)