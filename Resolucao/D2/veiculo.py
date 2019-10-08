class Veiculo:
    def __init__(self, nome, placa, modelo, ano):
        self.nome = nome
        self.placa = placa
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f'{self.nome} - {self.placa} - {self.modelo} - {self.ano}'