class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos."

nome= input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))
pessoa = Pessoa(nome=nome, idade=idade)
print(pessoa.apresentar())
