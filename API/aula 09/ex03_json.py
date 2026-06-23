from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/produtos/<int:id>")
def buscar_produto(id):

 produtos = [
     {"id": 1, "nome": "notebook", "preco": 3500.00, "disponivel": True},
    {"id": 2, "nome": "mouse", "preco": 150.00, "disponivel": True},
    {"id": 3, "nome": "teclado", "preco": 250.00, "disponivel": False},
    {"id": 4, "nome": "monitor'", "preco": 900.00, "disponivel": True}
]


 for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
 return jsonify({"erro": "produto nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)