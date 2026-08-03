from flask import Flask, jsonify
from ex01_relacao import conectar, criar_tabelas

app = Flask(__name__)

@app.route("/livros-completo", methods=["GET"])
def livros_completo():
    conexao = conectar()
    cursor = conexao.execute("""
        SELECT livros.id,
               livros.titulo,
               autores.nome AS autor
        FROM livros
        JOIN autores ON livros.autor_id = autores.id
    """)
    resultado = [dict(l) for l in cursor.fetchall()]
    conexao.close()
    return jsonify(resultado)

if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)