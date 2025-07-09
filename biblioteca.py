import sqlite3
from livro import Livro

class Biblioteca:
    def __init__(self):
        """Cria a tabela no banco se ainda não existir."""
        self._criar_tabela()

    def _conectar(self):
        """Conecta ao banco de dados."""
        return sqlite3.connect("biblioteca.db")

    def _criar_tabela(self):
        """Cria a tabela de livros no banco."""
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano TEXT NOT NULL,
                isbn TEXT UNIQUE NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def adicionar_livro(self, livro):
        """Adiciona um novo livro ao banco."""
        try:
            conn = self._conectar()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO livros (titulo, autor, ano, isbn)
                VALUES (?, ?, ?, ?)
            """, (livro.titulo, livro.autor, livro.ano, livro.isbn))
            conn.commit()
            print("✅ Livro adicionado com sucesso!")
        except sqlite3.IntegrityError:
            print("❌ ISBN já existente. Livro duplicado não foi adicionado.")
        finally:
            conn.close()

    def listar_livros(self):
        """Retorna todos os livros do banco como objetos Livro."""
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT titulo, autor, ano, isbn FROM livros")
        linhas = cursor.fetchall()
        conn.close()
        return [Livro(*linha) for linha in linhas]

    def buscar_por_titulo(self, palavra):
        """Busca livros com a palavra no título (sem case sensitive)."""
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT titulo, autor, ano, isbn FROM livros
            WHERE LOWER(titulo) LIKE ?
        """, (f"%{palavra.lower()}%",))
        resultados = cursor.fetchall()
        conn.close()
        livros = [Livro(*linha) for linha in resultados]
        if not livros:
            print(f"🔍 Nenhum livro encontrado com '{palavra}' no título.")
        return livros

    def remover_livro_por_isbn(self, isbn):
        """Remove um livro com o ISBN informado."""
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE isbn = ?", (isbn,))
        conn.commit()
        if cursor.rowcount == 0:
            print("❌ Nenhum livro com esse ISBN foi encontrado.")
        else:
            print("✅ Livro removido com sucesso!")
        conn.close()
