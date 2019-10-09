class Pessoa:
    def __init__(self, nome, dt_nascimento, endereco):
        self.nome = nome
        self.endereco = endereco
        self.dt_nascimento = dt_nascimento
        
    def __str__(self):
        return f'{self.nome} - {self.dt_nascimento} - {self.endereco}'