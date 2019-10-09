def cria_cadastro(nome, sobrenome, idade, cpf):
    return {'nome' : nome, 'sobrenome' : sobrenome, 'idade' : idade, 'cpf' : cpf }

def cria_menu():
    print('='*30)
    print('0 - Sair')
    print('1 - Cadastrar')
    print('2 - Listar Todos')
    print('='*30)

def ler_aluno():
    nome = input('Nome:')
    sobrenome = input('Sobrenome:')
    idade = int(input('Idade:'))
    cpf = input('CPF:')
    return cria_cadastro(nome, sobrenome, idade, cpf)

def valida_cpf(cpf):
    for a in lista_alunos:
        if a['cpf'] == cpf:
            return False    
    return True

lista_alunos = []
opcao =3

while opcao != 0:
    cria_menu()
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        aluno = ler_aluno()

        if valida_cpf(aluno['cpf']) :
            lista_alunos.append(aluno)       
        else:
            print('Cpf ja cadastrado') 

    elif opcao == 2:
        for i in lista_alunos:
            print(i)

#print(aluno)
