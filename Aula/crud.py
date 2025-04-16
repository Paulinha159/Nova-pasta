
usuarios = []

while True:
    print("\n MENU ")
    print("1 - criar usúario")
    print("2 - listar usúarios")
    print("3 - Atualizar Usúario")
    print("4 - Remover usúario")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        cidade = input("Digite sua cidade: ")
        profissao = input("Digite sua profissão: ")

        # Cria um dicionário para o usuário
        usuario = {
            "nome": nome,
            "idade": idade,
            "cidade": cidade,
            "profissão": profissao
        }

        # Adiciona o usuário à lista
        usuarios.append(usuario)
        print(f"Usuário {nome} adicionado com sucesso!")

    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("\nLista de usuários:")
            for usuario in usuarios:
                print(f"\nInformações de {usuario['nome']}:")
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")

    elif opcao == "3":
        nome = input("Digite o nome do usuário que deseja atualizar: ")
        encontrado = False
        for usuario in usuarios:
            if usuario["nome"].lower() == nome.lower():
                encontrado = True
                novo_nome = input("Novo nome: ")
                nova_idade = input("Nova idade: ")
                nova_cidade = input("Nova cidade: ")
                nova_profissao = input("Nova profissão: ")

                # Atualiza as informações do usuário
                usuario["nome"] = novo_nome
                usuario["idade"] = nova_idade
                usuario["cidade"] = nova_cidade
                usuario["profissão"] = nova_profissao
                print("Usuário atualizado com sucesso!")
                break
        if not encontrado:
            print("Usuário não encontrado.")

    elif opcao == "4":
        nome = input("Digite o nome do usuário que deseja remover: ")
        encontrado = False
        for usuario in usuarios:
            if usuario["nome"].lower() == nome.lower():
                usuarios.remove(usuario)
                print(f"Usuário {nome} removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Usuário não encontrado.")

    elif opcao == "5":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")


