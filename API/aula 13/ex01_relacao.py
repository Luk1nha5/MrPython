import sqlite3

BANCO = "biblioteca.db"

def conectar():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabelas():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
    """)

    conexao.commit()
    conexao.close()

def inserir_dados():
    conexao = conectar()

    conexao.execute("INSERT INTO autores (nome) VALUES (?)", ("Machado de Assis",))
    conexao.execute("INSERT INTO autores (nome) VALUES (?)", ("Jorge Amado",))

    conexao.execute(
        "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
        ("Dom Casmurro", 1)
    )
    conexao.execute(
        "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
        ("Capitães de Areia", 1)
    )
    conexao.execute(
        "INSERT INTO livros (titulo, autor_id) VALUES (?, ?)",
        ("Pequeno príncipe", 2)
    )

    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_tabelas()
    inserir_dados()
    print("Tabelas criadas e dados inseridos com sucesso!")