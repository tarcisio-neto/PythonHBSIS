

class Carro(Veiculo):
    def __init__(self, nome, placa, modelo, ano, n_portas, n_lugares)
    super().if __init__(nome, placa, modelo, ano)
    self.n_portas = n_portas
    self.n_lugares = n_lugares

    def __str__(self)
        return f'{ super().__str__()} - {self.n_portas} - {self.n_lugares}'