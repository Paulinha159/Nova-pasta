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

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario.exibir_info())

    def atualizar_usuario(self, user_id, novo_nome, novo_email):
        for usuario in self.usuarios:
            if usuario.id == user_id:
                usuario.nome = novo_nome
                usuario.email = novo_email
                return True
        return False

    def remover_usuario(self, user_id):
        self.usuarios = [u for u in self.usuarios if u.id != user_id]

# Menu de teste:
gerenciador = GerenciadorUsuarios()

gerenciador.adicionar_usuario(Usuario(1, "Alice", "alice@email.com"))
gerenciador.adicionar_usuario(Usuario(2, "Bob", "bob@email.com"))

print("Usuários cadastrados:")
gerenciador.listar_usuarios()

gerenciador.atualizar_usuario(1, "Alicia", "alicia@email.com")

print("\nApós atualização:")
gerenciador.listar_usuarios()

gerenciador.remover_usuario(2)

print("\nApós remoção:")
gerenciador.listar_usuarios()
