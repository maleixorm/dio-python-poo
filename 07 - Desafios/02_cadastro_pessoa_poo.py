class Pessoa:
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

#TODO: Crie um método para retornar as informações formatas com Nome e Idade:    
    def __str__(self):
        return f"{', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

# Entrada do usuário
nome = input()
idade = int(input())

# TODO: Crie uma instância da pessoa:
p1 = Pessoa(nome, idade)

#TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
print(p1)