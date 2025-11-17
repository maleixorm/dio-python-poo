class Bicicleta:
    def __init__(self, cor, marca, ano, valor):
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta Parada!")

    def correr(self):
        print("Vrummmmm....")

b1 = Bicicleta("preta", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.marca, b1.ano, b1.valor)