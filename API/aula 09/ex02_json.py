from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/produtos")
def listar_produtos():

  produtos = [
    {"id": 1, "nome": "notebook", "preco": 3500.00, "disponivel": True},
    {"id": 2, "nome": "mouse", "preco": 150.00, "disponivel": True},
    {"id": 3, "nome": "teclado", "preco": 250.00, "disponivel": False},
    {"id": 4, "nome": "monitor'", "preco": 900.00, "disponivel": True}
]
  return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)