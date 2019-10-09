class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome):
        super().__init__(nome)
        self.cpf = cpf
    def __str__(self):
        return f'{super().__str__()} - {self.cpf}'


class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome):
        super().__init__(nome)
        self.cnpj = cnpj
    def __str__(self):
        return f'{super().__str__()} - {self.cnpj}'

pessoa = PessoaFisica('738264938','josé') 
pessoa_juridica = PessoaJuridica('328758723578', 'Proway') 

lista_pessoas = [pessoa, pessoa_juridica]

for i in lista_pessoas:
    print (i)

