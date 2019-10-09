
class Moto(Veiculo):
    def __init__(self, nome, placa, modelo, ano, cilindros):
        super().__init__(nome, placa, modelo, ano)
        self.cilindros = cilindros

    def __str__(self):
        return f'{ super().__str__()} - {self.cilindros}'
        
        











