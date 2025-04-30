class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

pedido = Pedido("Carlos")
pedido.adicionar_item(Item("Hamburguer", 25))
pedido.adicionar_item(Item("Refrigerante", 5))

print(f"Total do pedido de {pedido.cliente}: R$ {pedido.calcular_total()}")
