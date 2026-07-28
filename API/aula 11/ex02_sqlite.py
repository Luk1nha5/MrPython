import sqlite3

conexao = sqlite3.connect("loja.db")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()

print("produtos")
for produto in produtos:
    print(dict(produto))

conexao.close()