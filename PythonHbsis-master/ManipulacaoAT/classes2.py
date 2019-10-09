class ContaBancaria:
    def __init__(self, numero, tipo, saldo, agencia=1888):
        self.agencia = agencia
        self.__numero = numero
        self.tipo = tipo
        self.__saldo = saldo
    
    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        self.__saldo = valor

    def depositar(self, deposito ):
        self.__saldo += deposito

    def sacar(self, saque):
        self.__saldo -= saque

    @property
    def numero(self):
        return self.__numero
    
    
conta_lais = ContaBancaria(35122, 17, 15111.45)

conta_lais.depositar(100)
conta_lais.sacar(11)

print('='*50)
print('\n'*3)


print( conta_lais.get_saldo() )
print( conta_lais.agencia )

#conta_lais.numero = 1421122
print( conta_lais.numero )

print('\n'*3)
print('='*50)