tarefas = {}

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ").strip().lower()
    if nome in tarefas:
        print("Essa tarefa já foi adicionada.")
        return

    descricao = input("Digite a descrição da tarefa (opcional, pode deixar em branco): ").strip()
    status = input("A tarefa está pendente ou concluída? (Digite 'pendente' ou 'concluída'): ").strip().lower()
    if status not in ["pendente", "concluída"]:
        print("Status inválido. Use 'pendente' ou 'concluída'.")
        return

    tarefas[nome] = {"descricao": descricao, "status": status}
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nTarefas cadastradas:")
        for nome, dados in tarefas.items():
            descricao = dados["descricao"] if dados["descricao"] else "Sem descrição"
            print(f"Nome: {nome.title()}")
            print(f"Descrição: {descricao}")
            print(f"Status: {dados['status'].capitalize()}")
            print("-" * 30)

def alterar_status():
    nome = input("Digite o nome da tarefa que deseja alterar: ").strip().lower()
    if nome not in tarefas:
        print("Tarefa não encontrada.")
        return

    print(f"Descrição atual: {tarefas[nome]['descricao'] or 'Sem descrição'}")
    nova_descricao = input("Digite a nova descrição (ou deixe em branco para manter a atual): ").strip()
    print(f"Status atual: {tarefas[nome]['status'].capitalize()}")
    novo_status = input("Digite o novo status da tarefa (pendente ou concluída): ").strip().lower()
    if novo_status not in ["pendente", "concluída"]:
        print("Status inválido. Use 'pendente' ou 'concluída'.")
        return

    if nova_descricao:
        tarefas[nome]["descricao"] = nova_descricao
    tarefas[nome]["status"] = novo_status
    print("Tarefa atualizada com sucesso!")

def remover_tarefa():
    nome = input("Digite o nome da tarefa que deseja remover: ").strip().lower()
    if nome not in tarefas:
        print("Tarefa não encontrada.")
        return

    del tarefas[nome]
    print("Tarefa removida com sucesso!")

while True:
    print("\nMENU DE GERENCIAMENTO DE TAREFAS")
    print("Escolha uma das opções abaixo:")
    print("1 - Adicionar uma nova tarefa")
    print("2 - Listar todas as tarefas cadastradas")
    print("3 - Alterar a descrição ou o status de uma tarefa")
    print("4 - Remover uma tarefa existente")
    print("5 - Sair do programa")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        alterar_status()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        print("Saindo do programa... Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


