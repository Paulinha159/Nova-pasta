 # Supermercado Inteligente Interativo

supermercado = {
    "Arroz": 5.49,
    "Feijão": 7.20,
    "Macarrão": 3.10,
    "Leite": 4.00,
    "Pão": 0.80,
    "Ovos": 10.00
}

def exibir_menu():
    print("\n MENU SUPERMERCADO INTELIGENTE")
    print("1. Adicionar produto ao carrinho")
    print("2. Visualizar carrinho")
    print("3. Finalizar compra")
    print("4. Sair")

carrinho = {}

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("\n--- Produtos Disponíveis ---")
            for produto, preco in supermercado.items():
                print(f"{produto}: R$ {preco:.2f}")

            nome_produto = input("Digite o nome do produto que deseja adicionar: ").title()

            if nome_produto in supermercado:
                quantidade = int(input("Digite a quantidade: "))
                if nome_produto in carrinho:
                    carrinho[nome_produto] += quantidade
                else:
                    carrinho[nome_produto] = quantidade
                print(f"{quantidade}x {nome_produto} adicionado(s) ao carrinho.")
            else:
                print("Produto não encontrado no supermercado.")

        case "2":
            if not carrinho:
                print("Carrinho vazio.")
            else:
                print("\n--- Seu Carrinho ---")
                total = 0
                for produto, qtd in carrinho.items():
                    preco_unitario = supermercado[produto]
                    subtotal = preco_unitario * qtd
                    print(f"{produto} - {qtd}x R$ {preco_unitario:.2f} = R$ {subtotal:.2f}")
                    total += subtotal
                print(f"TOTAL: R$ {total:.2f}")

        case "3":
            if not carrinho:
                print("Carrinho vazio. Nada para finalizar.")
            else:
                print("\n--- Finalizando Compra ---")
                total = 0
                for produto, qtd in carrinho.items():
                    total += supermercado[produto] * qtd
                print(f"Valor total da compra: R$ {total:.2f}")
                continuar = input("Deseja fazer uma nova compra? (s/n): ").lower()
                if continuar == "s":
                    carrinho.clear()
                else:
                    print("Obrigado por comprar conosco!")
                    break

        case "4":
            print("Saindo do sistema. Volte sempre!")
            break

        case _:
            print("Opção inválida. Tente novamente.")
