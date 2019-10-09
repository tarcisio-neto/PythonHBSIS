numero_banco = 160

def cria_conta(nome, numero_conta, saldo):   
    return {'nome':nome, 'numero_c':numero_conta, 'saldo':saldo }

def depositar(cnt, valor):
    cnt['saldo'] += valor
    
def sacar(cnt,valor):
    cnt['saldo'] -= valor

def imprimir_n_b():
    print(numero_banco)