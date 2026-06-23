from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/produto")
def produto():

    dados_produto = {
        "id": 1,
        "nome": "mouse",
        "preco": 350.00,
        "disponivel": True
    }
    return jsonify(dados_produto)

if __name__ == "__main__":
    app.run(debug=True)