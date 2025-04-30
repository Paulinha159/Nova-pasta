def cadastrar_aluno(lista_alunos):
    nome = " ".join(input("Digite o nome do aluno: ").strip().lower().split())
    if nome in lista_alunos:
        print(f"Aluno '{nome.title()}' já está cadastrado.")
        return

    idade = input("Digite a idade do aluno: ").strip()
    if not idade.isdigit() or int(idade) <= 0:
        print("Erro: A idade deve ser um número inteiro positivo.")
        return
    idade = int(idade)

    notas = []
    while True:
        nota = input("Digite uma nota (ou digite 'sair' para finalizar): ").strip().lower()
        if nota == "sair" or nota == "s":
            if not notas:
                print("Erro: É necessário adicionar pelo menos uma nota.")
            else:
                break
        elif nota.replace('.', '', 1).isdigit():
            nota = float(nota)
            if 0 <= nota <= 10:
                notas.append(nota)
                print("Nota adicionada com sucesso!")
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        else:
            print("Erro: A nota deve ser um número válido.")

    media = sum(notas) / len(notas)

    lista_alunos[nome] = {
        "nome": nome.title(),
        "idade": idade,
        "notas": notas,
        "media": media
    }
    print(f"Aluno '{nome.title()}' cadastrado com sucesso!")

def listar_alunos(lista_alunos):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nLista de Alunos:")
        for nome, dados in lista_alunos.items():
            print(f"Nome: {dados['nome']}")
            print(f"Idade: {dados['idade']}")
            print(f"Notas: {', '.join(map(str, dados['notas']))}")
            print(f"Média: {dados['media']:.2f}")
            print("-" * 30)

def atualizar_aluno(lista_alunos):
    nome = " ".join(input("Digite o nome do aluno que deseja atualizar: ").strip().lower().split())
    if nome not in lista_alunos:
        print("Aluno não encontrado.")
        return

    print("\nAtualize as informações do aluno. Deixe em branco para manter o valor atual.")

    novo_nome = input(f"Novo nome ({lista_alunos[nome]['nome']}): ").strip()
    if novo_nome:
        novo_nome = " ".join(novo_nome.lower().split())
        if novo_nome != nome and novo_nome in lista_alunos:
            print(f"Erro: Já existe um aluno com o nome '{novo_nome.title()}'.")
            return
        lista_alunos[novo_nome] = lista_alunos.pop(nome)
        lista_alunos[novo_nome]["nome"] = novo_nome.title()
        nome = novo_nome

    nova_idade = input(f"Nova idade ({lista_alunos[nome]['idade']}): ").strip()
    if nova_idade:
        if not nova_idade.isdigit() or int(nova_idade) <= 0:
            print("Erro: A idade deve ser um número inteiro positivo.")
            return
        lista_alunos[nome]["idade"] = int(nova_idade)

    print("\nMini Menu de Notas:")
    print("1 - Atualizar notas")
    print("2 - Manter notas atuais")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novas_notas = []
        while True:
            nota = input("Digite uma nota (ou digite 'sair' para finalizar): ").strip().lower()
            if nota == "sair" or nota == "s":
                if not novas_notas:
                    print("Erro: É necessário adicionar pelo menos uma nota.")
                else:
                    break
            elif nota.replace('.', '', 1).isdigit():
                nota = float(nota)
                if 0 <= nota <= 10:
                    novas_notas.append(nota)
                    print("Nota adicionada com sucesso!")
                else:
                    print("Erro: A nota deve estar entre 0 e 10.")
            else:
                print("Erro: A nota deve ser um número válido.")

        lista_alunos[nome]["notas"] = novas_notas
        lista_alunos[nome]["media"] = sum(novas_notas) / len(novas_notas)

    print(f"Aluno '{lista_alunos[nome]['nome']}' atualizado com sucesso!")

def remover_aluno(lista_alunos):
    nome = " ".join(input("Digite o nome do aluno que deseja remover: ").strip().lower().split())
    if nome in lista_alunos:
        del lista_alunos[nome]
        print(f"Aluno '{nome.title()}' removido com sucesso!")
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
        cadastrar_aluno(lista_alunos)
    elif opcao == "2":
        listar_alunos(lista_alunos)
    elif opcao == "3":
        atualizar_aluno(lista_alunos)
    elif opcao == "4":
        remover_aluno(lista_alunos)
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")


