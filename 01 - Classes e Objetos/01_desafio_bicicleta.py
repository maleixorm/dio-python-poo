class Bicicleta:
    def __init__(self, cor, marca, ano, valor, aro=22):
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = 1

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta Parada!")

    def correr(self):
        print("Vrummmmm....")

    def trocarMarcha(self, nro_marcha):
        print("Marcha trocada...")
        _self = self

        def _trocar_marcha():
            if nro_marcha > _self.marcha:
                print("Marcha trocada...")
            else:
                print("Não foi possível trocar de marcha...")

    # def __str__(self):
    #     return f"{self.__class__.__name__} -  Cor: {self.cor}, Marca: {self.marca}, Ano: {self.ano}, Valor: {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("preta", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.marca, b1.ano, b1.valor)

b2 = Bicicleta("vermelha", "monark", 2000, 189)
b2.buzinar() # Bicicleta.buzinar(b2)
print(b1)
print(b2)
b2.trocarMarcha()