from conta import cria_conta, sacar, depositar
def conta_existe(cnttt):
    if(cnttt):
        return True
    else:
        return False

def gera_menu():
    print('{}0-Criar'.format(' '*5))
    print('{}1-Saque'.format(' '*5))
    print('{}2-Deposito'.format(' '*5))
    print('{}3-Sair'.format(' '*5))
    print('{}'.format('-'*10))


print('=='*50)
cnt1 = {}
opc = 0
while opc !=3:
    gera_menu()
    opc = int(input('Digite uma opção: ') )

    if(opc==0):
        n = input('{}Digite o nome : '.format(' '*5))
        nu = int(input('{}Digite o numero : '.format(' '*5)))
        sa = float(input('{}Digite o saldo inicial : '.format(' '*5)))
        cnt1 = cria_conta(n, nu, sa)
    elif(opc==1):
        if(conta_existe(cnt1)):
            saque = float(input('{}Digite o valor do saque : '.format(' '*5)))
            sacar(cnt1, saque)
        else:
            print('Nenhuma conta criada! Acesse a opção 0 do menu. ')
    elif(opc==2):
        if(conta_existe(cnt1)):
            deposito = float(input('{}Digite o valor do deposito : '.format(' '*5)))
            depositar(cnt1, deposito)           
        else:
            print('Nenhuma conta criada! Acesse a opção 0 do menu. ')
    elif(opc!=3):
        print('Digite uma opcao valida')
    print(cnt1)
print('=='*50)