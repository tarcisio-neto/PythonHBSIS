class Produto:
    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__descricao = ''
        self.__categoria_id = 0
        self.__estoque_id = 0

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self,descricao):
        self.__descricao = descricao

    @property
    def categoria_id(self):
        return self.__categoria_id
    @categoria_id.setter
    def categoria_id(self,categoria_id):
        self.__categoria_id = categoria_id

    @property
    def __estoque_id(self):
        return self.__estoque_id
    @estoque_id.setter
    def estoque_id(self,estoque_id):
        self.__estoque_id = estoque_id