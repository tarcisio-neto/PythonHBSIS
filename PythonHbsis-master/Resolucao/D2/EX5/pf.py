from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, dt_nascimento, endereco):
        super().__init__(nome, dt_nascimento, endereco)
        self.cpf = cpf

    def __str__(self):
        return f'{ super().__str__() } - {self.cpf}'