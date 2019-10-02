class Alunos:
    def __init__(self,nome, sobrenome,telefone):
        self.Nome = nome
        self.Telefone = telefone
        self.Sobrenome = sobrenome
    def nome_completo(self):
        nomecompleto = self.Nome + ' ' + self.Sobrenome
        return nomecompleto