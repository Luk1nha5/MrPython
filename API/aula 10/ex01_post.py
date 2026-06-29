from flask import Flask, jsonify, request
app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "teclado", "preco": 199.90},
]

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos), 200

@app.route("/produtos", methods=["POST"])
def criar_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)

    return jsonify(novo_produto), 201
if __name__ == "__main__":
    app.run(debug=True)