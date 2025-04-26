usuarios = {}

while True:
    print("\n MENU ")
    print("1 - Criar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Remover usuário")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite seu nome: ").strip().lower()
        if nome in usuarios:
            print("Usuário já existe. Tente outro nome.")
            continue

        idade = input("Digite sua idade: ")
        cidade = input("Digite sua cidade: ")
        profissao = input("Digite sua profissão: ")

        usuarios[nome] = {
            "nome": nome.title(),
            "idade": idade,
            "cidade": cidade,
            "profissão": profissao
        }
        print(f"Usuário {nome.title()} adicionado com sucesso!")

    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("\nLista de usuários:")
            for nome, dados in usuarios.items():
                print(f"\nInformações de {dados['nome']}:")
                for chave, valor in dados.items():
                    print(f"{chave.capitalize()}: {valor}")

    elif opcao == "3":
        nome = input("Digite o nome do usuário que deseja atualizar: ").strip().lower()
        if nome in usuarios:
            novo_nome = input("Novo nome: ").strip().lower()
            nova_idade = input("Nova idade: ")
            nova_cidade = input("Nova cidade: ")
            nova_profissao = input("Nova profissão: ")

            usuarios[nome] = {
                "nome": novo_nome.title(),
                "idade": nova_idade,
                "cidade": nova_cidade,
                "profissão": nova_profissao
            }
            print("Usuário atualizado com sucesso!")
        else:
            print("Usuário não encontrado.")

    elif opcao == "4":
        nome = input("Digite o nome do usuário que deseja remover: ").strip().lower()
        if nome in usuarios:
            del usuarios[nome]
            print(f"Usuário {nome.title()} removido com sucesso!")
        else:
            print("Usuário não encontrado.")

    elif opcao == "5":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")


