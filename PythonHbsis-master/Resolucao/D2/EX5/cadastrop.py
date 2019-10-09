from pf import PessoaFisica
from pj import PessoaJuridica

def monta_menu():
    print("="*50)
    print("0-Sair")
    print("1-Cadastrar PF")
    print("2-Cadastrar PJ")
    print("3-Listar")
    print("="*50)

def cadastra_pf():
    print("PF")
    nome = input('Nome:')
    cpf = input('CPF:')
    dtnsc = input('Dt Nascimento:')
    end = input('End:')
    return PessoaFisica(nome, cpf, dtnsc, end)

def cadastra_pj():
    print("PJ")
    nome = input('Nome:')
    cnpj = input('CNPJ:')
    dtnsc = input('Dt Nascimento:')
    end = input('End:')
    return PessoaJuridica(nome, cnpj, dtnsc, end)

def listar():
    print("Lista")
    for p in lista:
        print( f"Pessoa : {p}" ) 

lista = []
opcao = 4

while opcao !=0:
    monta_menu()
    opcao = int(input("Digite uma opção:"))
    if opcao == 1:
        lista.append(cadastra_pf())
    elif opcao == 2:
        lista.append(cadastra_pj())
    elif opcao == 3:
        listar()
    

