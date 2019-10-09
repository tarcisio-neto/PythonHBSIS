


class Bier:
    @property
    def teor(self):
        print('Mae {}'.format(self))
        return self.__teor
    @teor.setter
    def teor(self, teor):
        self.__teor = teor

class Bebida(Bier):
    @property
    def tamanho(self):
        print('Filha {}'.format(self))
        return self.__tamanho
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

bebida = Bebida()
bebida.teor = 10
bebida.tamanho = '500ml'

print('='*50)
print('\n'*3)

print( bebida.teor )
print( bebida.tamanho )
print( bebida )


print('\n'*3)
print('='*50)