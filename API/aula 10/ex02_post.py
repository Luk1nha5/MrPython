from flask import Flask, jsonify, request
app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "teclado", "preco": 199.90}
]

@app.route("/produtos", methods=["POST"])
def criar_produto():
    novo_produto = request.get_json()

    if "preco" not in novo_produto:
        return jsonify({"erro": "campo preco obrigatorio"}), 400

    produtos.append(novo_produto)
    return jsonify(novo_produto), 201
if __name__ == "__main__":
    app.run(debug=True)