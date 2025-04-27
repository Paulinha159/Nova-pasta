def cadastrar_produto(estoque):
    nome = " ".join(input("Digite o nome do produto: ").strip().lower().split())  # Normaliza o nome
    if nome in estoque:
        print(f"Produto '{nome.title()}' já está cadastrado. Retornando ao menu principal.")
        return

    try:
        preco = float(input("Digite o preço do produto: "))
    except ValueError:
        print("Erro: O preço deve ser um número decimal.")
        return

    try:
        quantidade = int(input("Digite a quantidade do produto: "))
    except ValueError:
        print("Erro: A quantidade deve ser um número inteiro.")
        return

    estoque[nome] = {
        "nome": nome.title(),
        "preço": f"R$ {preco:.2f}",
        "quantidade": quantidade
    }
    print(f"Produto {nome.title()} cadastrado com sucesso!")


def listar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de produtos:")
        for nome, dados in estoque.items():
            print(f"\nInformações do produto {dados['nome']}:")
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")


def atualizar_produto(estoque):
    nome = " ".join(input("Digite o nome do produto que deseja atualizar: ").strip().lower().split())  # Normaliza o nome
    if nome not in estoque:
        print("Produto não encontrado.")
        return

    print("\nAtualize as informações do produto. Deixe em branco para manter o valor atual.")

    # Atualizar o nome
    novo_nome = " ".join(input(f"Novo nome ({estoque[nome]['nome']}): ").strip().lower().split())
    if novo_nome and novo_nome != nome and novo_nome in estoque:
        print(f"Erro: Já existe um produto com o nome '{novo_nome.title()}'.")
        return
    elif novo_nome:
        estoque[novo_nome] = estoque.pop(nome)
        estoque[novo_nome]["nome"] = novo_nome.title()
        nome = novo_nome  # Atualiza a referência do nome no dicionário

    # Atualizar o preço
    try:
        novo_preco = input(f"Novo preço ({estoque[nome]['preço']}): ").strip()
        if novo_preco:
            estoque[nome]["preço"] = f"R$ {float(novo_preco):.2f}"
    except ValueError:
        print("Erro: O preço deve ser um número decimal.")
        return

    # Atualizar a quantidade
    try:
        nova_quantidade = input(f"Nova quantidade ({estoque[nome]['quantidade']}): ").strip()
        if nova_quantidade:
            estoque[nome]["quantidade"] = int(nova_quantidade)
    except ValueError:
        print("Erro: A quantidade deve ser um número inteiro.")
        return

    print(f"Produto '{estoque[nome]['nome']}' atualizado com sucesso!")


def remover_produto(estoque):
    nome = " ".join(input("Digite o nome do produto que deseja remover: ").strip().lower().split())  # Normaliza o nome
    if nome in estoque:
        del estoque[nome]
        print(f"Produto {nome.title()} removido com sucesso!")
    else:
        print("Produto não encontrado.")


estoque = {}

while True:
    print("\n MENU ")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto(estoque)
    elif opcao == "2":
        listar_produtos(estoque)
    elif opcao == "3":
        atualizar_produto(estoque)
    elif opcao == "4":
        remover_produto(estoque)
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")


