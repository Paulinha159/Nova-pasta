class Usuario:
    def __init__(self, user_id, nome, email):
        self.id = user_id
        self.nome = nome
        self.email = email

    def exibir_info(self):
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}"

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []
        self.proximo_id = 1

    def adicionar_usuario(self, nome, email):
        usuario = Usuario(self.proximo_id, nome, email)
        self.usuarios.append(usuario)
        print(f"Usuário adicionado com sucesso! ID: {self.proximo_id}")
        self.proximo_id += 1  
    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.usuarios:
                print(usuario.exibir_info())

    def atualizar_usuario(self, user_id, novo_nome, novo_email):
        for usuario in self.usuarios:
            if usuario.id == user_id:
                usuario.nome = novo_nome
                usuario.email = novo_email
                print("Usuário atualizado com sucesso!")
                return True
        print("Usuário não encontrado.")
        return False

    def remover_usuario(self, user_id):
        for usuario in self.usuarios:
            if usuario.id == user_id:
                self.usuarios.remove(usuario)
                print("Usuário removido com sucesso!")
                return True
        print("Usuário não encontrado.")
        return False

# Menu interativo
gerenciador = GerenciadorUsuarios()

while True:
    print("\n--- MENU ---")
    print("1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Remover usuário")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        gerenciador.adicionar_usuario(nome, email)

    elif opcao == "2":
        gerenciador.listar_usuarios()

    elif opcao == "3":
        user_id = int(input("ID do usuário a atualizar: "))
        novo_nome = input("Novo nome: ")
        novo_email = input("Novo email: ")
        if not gerenciador.atualizar_usuario(user_id, novo_nome, novo_email):
            print("Usuário não encontrado.")

    elif opcao == "4":
        user_id = int(input("ID do usuário a remover: "))
        gerenciador.remover_usuario(user_id)

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
