class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def exibir_tipo(self):
        return "Tipo genérico de veículo"

class Carro(Veiculo):
    def exibir_tipo(self):
        return "Este é um carro"

class Moto(Veiculo):
    def exibir_tipo(self):
        return "Esta é uma moto"

# Exemplo de uso:
veiculos = [Carro("ford"), Moto("Yamaha")]
for v in veiculos:
    print(f"{v.marca}: {v.exibir_tipo()}")
