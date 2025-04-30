class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo}, por {livro.autor}")

titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
biblio = Biblioteca()
biblio.adicionar_livro(Livro(titulo, autor))
biblio.adicionar_livro(Livro("O Alquimista", "Paulo Coelho"))
biblio.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis"))
biblio.listar_livros()
