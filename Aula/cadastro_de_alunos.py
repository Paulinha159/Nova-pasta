def cadastrar_Aluno(lista_alunos):
    nome = " ".join(input("Digite o nome do Aluno: ").strip().lower().split())  # Normaliza o nome
    if nome in lista_alunos:
        print(f"Aluno '{nome.title()}' já está cadastrado. Retornando ao menu principal.")
        return

    try:
        idade = int(input("Digite a idade do Aluno: "))
    except ValueError:
        print("Erro: A idade deve ser um número inteiro.")
        return

    try:
        nota = float(input("Digite a nota do Aluno: "))
    except ValueError:
        print("Erro: A nota deve ser um número decimal.")
        return

    lista_alunos[nome] = {
        "nome": nome.title(),
        "idade": idade,
        "nota": nota
    }
    print(f"Aluno {nome.title()} cadastrado com sucesso!")


def listar_Alunos(lista_alunos):
    if not lista_alunos:
        print("Nenhum Aluno cadastrado.")
    else:
        print("\nLista de Alunos:")
        for nome, dados in lista_alunos.items():
            print(f"\nInformações do Aluno {dados['nome']}:")
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")


def atualizar_Aluno(lista_alunos):
    nome = " ".join(input("Digite o nome do Aluno que deseja atualizar: ").strip().lower().split())  # Normaliza o nome
    if nome not in lista_alunos:
        print("Aluno não encontrado.")
        return

    print("\nAtualize as informações do Aluno. Deixe em branco para manter o valor atual.")

    # Atualizar o nome
    novo_nome = " ".join(input(f"Novo nome ({lista_alunos[nome]['nome']}): ").strip().lower().split())
    if novo_nome and novo_nome != nome and novo_nome in lista_alunos:
        print(f"Erro: Já existe um Aluno com o nome '{novo_nome.title()}'.")
        return
    elif novo_nome:
        lista_alunos[novo_nome] = lista_alunos.pop(nome)
        lista_alunos[novo_nome]["nome"] = novo_nome.title()
        nome = novo_nome  # Atualiza a referência do nome no dicionário

    # Atualizar a idade
    try:
        nova_idade = input(f"Nova idade ({lista_alunos[nome]['idade']}): ").strip()
        if nova_idade:
            lista_alunos[nome]["idade"] = int(nova_idade)
    except ValueError:
        print("Erro: A idade deve ser um número inteiro.")
        return

    # Atualizar a nota
    try:
        nova_nota = input(f"Nova nota ({lista_alunos[nome]['nota']}): ").strip()
        if nova_nota:
            lista_alunos[nome]["nota"] = float(nova_nota)
    except ValueError:
        print("Erro: A nota deve ser um número decimal.")
        return

    print(f"Aluno '{lista_alunos[nome]['nome']}' atualizado com sucesso!")


def remover_Aluno(lista_alunos):
    nome = " ".join(input("Digite o nome do Aluno que deseja remover: ").strip().lower().split())  # Normaliza o nome
    if nome in lista_alunos:
        del lista_alunos[nome]
        print(f"Aluno {nome.title()} removido com sucesso!")
    else:
        print("Aluno não encontrado.")


lista_alunos = {}

while True:
    print("\n MENU ")
    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Atualizar Aluno")
    print("4 - Remover Aluno")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_Aluno(lista_alunos)
    elif opcao == "2":
        listar_Alunos(lista_alunos)
    elif opcao == "3":
        atualizar_Aluno(lista_alunos)
    elif opcao == "4":
        remover_Aluno(lista_alunos)
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")


