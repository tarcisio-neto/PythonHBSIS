class Cliente:
    def __init__(self):
        self.__id= 0
        self.__nome=''
        self.__cpf=''
        self.__nascimento=''

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def nascimento(self):
        return self.__nascimento                
    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento
