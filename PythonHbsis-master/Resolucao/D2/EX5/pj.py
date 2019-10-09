from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj, dt_nascimento, endereco):
        super().__init__(nome, dt_nascimento, endereco)
        self.cnpj = cnpj

    def __str__(self):
        return f'{super().__str__()} - {self.cnpj}'
    