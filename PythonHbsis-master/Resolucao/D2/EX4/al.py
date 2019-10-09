def cria_cadastro(nome, sobrenome, idade, cpf):
    return {'nome' : nome, 'sobrenome' : sobrenome, 'idade' : idade, 'cpf' : cpf }

lista_alunos = []
opcao =3

while opcao != 0:
    print('='*30)
    print('0 - Sair')
    print('1 - Cadastrar')
    print('2 - Listar Todos')
    print('='*30)
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        nome = input('Nome:')
        sobrenome = input('Sobrenome:')
        idade = int(input('Idade:'))
        cpf = input('CPF:')
        verificador = 0
        aluno = cria_cadastro(nome, sobrenome, idade, cpf)

        for a in lista_alunos:
            if a['cpf'] == cpf:
                verificador = 1 
                print('Cpf ja cadastrado')  
                
        if verificador == 0:
            lista_alunos.append(aluno)       

    elif opcao == 2:
        for i in lista_alunos:
            print(i)

#print(aluno)
