import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
""")

produtos = [
    ("teclado", 250.00),
    ("mouse", 120.50),
    ("monitor", 899.90)
]

cursor.executemany("INSERT INTO produtos (nome, preco) VALUES (?, ?)", produtos)
conexao.commit()
conexao.close()

print("banco loja.db")