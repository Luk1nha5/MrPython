from flask import Flask, jsonify, request
from ex01_relacao import conectar, criar_tabelas

app = Flask(__name__)

@app.route("/livros/por-autor", methods=["GET"])
def livros_do_autor():
    autor_id = request.args.get("autor_id")
    conexao = conectar()
    cursor = conexao.execute(
        "SELECT * FROM livros WHERE autor_id = ?",
        (autor_id,)
    )
    resultado = [dict(l) for l in cursor.fetchall()]
    conexao.close()
    return jsonify(resultado)

@app.route("/livros/busca", methods=["GET"])
def buscar_livros():
    termo = request.args.get("titulo")
    conexao = conectar()
    cursor = conexao.execute(
        "SELECT * FROM livros WHERE titulo LIKE ?",
        (f"%{termo}%",)
    )
    resultado = [dict(l) for l in cursor.fetchall()]
    conexao.close()
    return jsonify(resultado)

if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)