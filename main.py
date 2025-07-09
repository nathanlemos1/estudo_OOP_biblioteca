from livro import Livro
from biblioteca import Biblioteca

def mostrar_menu():
    print("\n📚 MENU DA BIBLIOTECA")
    print("1 - Listar todos os livros")
    print("2 - Adicionar novo livro")
    print("3 - Buscar livro por título")
    print("4 - Remover livro por ISBN")
    print("5 - Sair")

def listar_livros(biblioteca):
    livros = biblioteca.listar_livros()
    if livros:
        print("\n📖 LIVROS NA BIBLIOTECA:")
        for livro in livros:
            print(livro)

def adicionar_livro(biblioteca):
    print("\n➕ ADICIONAR NOVO LIVRO:")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    isbn = input("ISBN: ")
    novo_livro = Livro(titulo, autor, ano, isbn)
    biblioteca.adicionar_livro(novo_livro)
    print("✅ Livro adicionado com sucesso!")

def buscar_livro(biblioteca):
    termo = input("\n🔍 Digite uma palavra do título: ")
    resultados = biblioteca.buscar_por_titulo(termo)
    if resultados:
        print("\n📘 LIVROS ENCONTRADOS:")
        for livro in resultados:
            print(livro)

def remover_livro(biblioteca):
    isbn = input("\n❌ Digite o ISBN do livro a remover: ")
    biblioteca.remover_livro_por_isbn(isbn)

def main():
    biblioteca = Biblioteca()

    # Exemplo de livros pré-cadastrados (opcional)
    biblioteca.adicionar_livro(Livro("Python para Iniciantes", "Nathan Lemos", 2022, "123456789"))
    biblioteca.adicionar_livro(Livro("Aprendendo POO", "Maria Silva", 2020, "987654321"))

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (1 a 5): ")

        if opcao == "1":
            listar_livros(biblioteca)
        elif opcao == "2":
            adicionar_livro(biblioteca)
        elif opcao == "3":
            buscar_livro(biblioteca)
        elif opcao == "4":
            remover_livro(biblioteca)
        elif opcao == "5":
            print("\n👋 Programa encerrado. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
