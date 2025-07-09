import sqlite3

def conectar():
    return sqlite3.connect("biblioteca.db")

def criar_tabela():
    conn = conectar()
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
