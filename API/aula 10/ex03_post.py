from flask import Flask, jsonify, request
app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "MR C", "DEUS": False}
]

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas), 200

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova_tarefa = request.get_json()
    

    if "titulo" not in nova_tarefa:
        return jsonify({"erro": "titulo obrigatorio"}), 400
        
    if not nova_tarefa["titulo"].strip():
        return jsonify({"erro": "o titulo não pode estar em branco"}), 400
 
    if "feita" not in nova_tarefa:
        nova_tarefa["feita"] = False

    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201
if __name__ == "__main__":
    app.run(debug=True)