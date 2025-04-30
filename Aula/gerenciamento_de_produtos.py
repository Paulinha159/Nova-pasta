def cadastrar_produto(estoque):
    nome = input("Digite o nome do produto: ").strip().lower()  # Armazena o nome em minúsculas
    if nome in estoque:
        print(f"Produto '{nome.title()}' já está cadastrado.")
        return

    preco = input("Digite o preço do produto: ").strip()
    if not preco.replace('.', '', 1).isdigit():
        print("Erro: O preço deve ser um número.")
        return
    preco = float(preco)

    quantidade = input("Digite a quantidade do produto: ").strip()
    if not quantidade.isdigit():
        print("Erro: A quantidade deve ser um número inteiro.")
        return
    quantidade = int(quantidade)

    estoque[nome] = {"nome": nome.title(), "preço": preco, "quantidade": quantidade}
    print(f"Produto '{nome.title()}' cadastrado com sucesso!")


def listar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de produtos:")
        for produto in estoque.values():
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preço']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            print("-" * 20)


def atualizar_produto(estoque):
    nome = input("Digite o nome do produto que deseja atualizar: ").strip().lower()  # Busca o nome em minúsculas
    if nome not in estoque:
        print("Produto não encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")

    novo_nome = input(f"Novo nome ({estoque[nome]['nome']}): ").strip()
    if novo_nome:
        novo_nome = novo_nome.lower()
        if novo_nome != nome and novo_nome in estoque:
            print(f"Erro: Já existe um produto com o nome '{novo_nome.title()}'.")
            return
        estoque[novo_nome] = estoque.pop(nome)
        estoque[novo_nome]["nome"] = novo_nome.title()
        nome = novo_nome

    novo_preco = input(f"Novo preço ({estoque[nome]['preço']}): ").strip()
    if novo_preco:
        if not novo_preco.replace('.', '', 1).isdigit():
            print("Erro: O preço deve ser um número.")
            return
        estoque[nome]["preço"] = float(novo_preco)

    nova_quantidade = input(f"Nova quantidade ({estoque[nome]['quantidade']}): ").strip()
    if nova_quantidade:
        if not nova_quantidade.isdigit():
            print("Erro: A quantidade deve ser um número inteiro.")
            return
        estoque[nome]["quantidade"] = int(nova_quantidade)

    print(f"Produto '{estoque[nome]['nome']}' atualizado com sucesso!")


def remover_produto(estoque):
    nome = input("Digite o nome do produto que deseja remover: ").strip().lower()  # Busca o nome em minúsculas
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome.title()}' removido com sucesso!")
    else:
        print("Produto não encontrado.")


estoque = {}

while True:
    print("\nMENU")
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


