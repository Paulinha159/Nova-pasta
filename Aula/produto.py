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

# Exemplo de uso:
produto = Produto("Camisa", 100.0)
print("Produto:", produto.get_nome())
print("Preço original: R$", produto.get_preco())
print("Preço com 10% de desconto: R$", produto.aplicar_desconto(10))
