class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligarMotor(self):
        print("Ligando o motor!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    
    def estaCarregado(self):
        print(f"{'Estou' if self.carregado else 'Não estou'} carregado!")


moto = Motocicleta("Preta", "ABC-1234", 2)
print(moto)
moto.ligarMotor()

carro = Carro("Prata", "ZYX-9876", 4)
print(carro)
carro.ligarMotor()

caminhao = Caminhao("Roxo", "GHI-4567", 8, False)
print(caminhao)
caminhao.ligarMotor()
caminhao.estaCarregado()