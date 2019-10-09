



class Pessoa:
    def __init__(self, cpf):
        print('Chegou na mae {}'.format(cpf))
        self.cpf = cpf        
    @property
    def nome(self):
        print(self)
        return  self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

class Aluno(Pessoa):
    # def __init__(self, cpf):
    #     super().__init__(cpf)
        
    @property
    def matricula(self):
        print(self)
        return  self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula




al = Aluno('12354136513156')