class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def aplicar_desconto(self, percentual):
        desconto = self.__preco * (percentual / 100)
        return self.__preco - desconto

nome = input("Digite o nome do produto: ")
valor= float(input("Digite o preço do produto: "))
produtos = Produto(nome= nome, preco= valor)
print("Produto:", produtos.get_nome())
print("Preço original: R$", produtos.get_preco())
print("Preço com 10% de desconto: R$", produtos.aplicar_desconto(10))
