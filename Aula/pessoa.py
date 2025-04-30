class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos."

# Exemplo de uso:
pessoa = Pessoa("Ana", 22)
print(pessoa.apresentar())
