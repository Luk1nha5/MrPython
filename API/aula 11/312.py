import sqlite3

conexao = sqlite3.connect("loja.db") # 
cursor = conexao.cursor() # [cite: 22]

cursor.execute("DELETE FROM produtos")

conexao.commit() # [cite: 30, 32]
conexao.close() # [cite: 31, 33]

print("Todos os produtos foram apagados!")