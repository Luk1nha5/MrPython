from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = "biblioteca.db"

# conexao com o banco
def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row 
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nacionalidade TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            ano_publicacao INTEGER,
            autor_id INTEGER NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES autores(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()



# CRUD - autores (tabela pai)


@app.route("/autores", methods=["GET"])
def listar_autores():
    conn = get_conn()
    autores = conn.execute("SELECT * FROM autores").fetchall()
    conn.close()
    return jsonify([dict(a) for a in autores])


@app.route("/autores/<int:autor_id>", methods=["GET"])
def buscar_autor(autor_id):
    conn = get_conn()
    autor = conn.execute("SELECT * FROM autores WHERE id = ?", (autor_id,)).fetchone()
    conn.close()

    if autor is None:
        return jsonify({"erro": "Autor não encontrado"}), 404

    return jsonify(dict(autor))


@app.route("/autores", methods=["POST"])
def criar_autor():
    dados = request.get_json(silent=True) or {}
    nome = dados.get("nome")
    nacionalidade = dados.get("nacionalidade")

    if not nome:
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO autores (nome, nacionalidade) VALUES (?, ?)",
        (nome, nacionalidade)
    )
    conn.commit()
    novo_id = cur.lastrowid
    conn.close()

    return jsonify({"id": novo_id, "nome": nome, "nacionalidade": nacionalidade}), 201


@app.route("/autores/<int:autor_id>", methods=["PUT"])
def atualizar_autor(autor_id):
    dados = request.get_json(silent=True) or {}
    nome = dados.get("nome")
    nacionalidade = dados.get("nacionalidade")

    if not nome:
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400

    conn = get_conn()
    autor = conn.execute("SELECT * FROM autores WHERE id = ?", (autor_id,)).fetchone()
    if autor is None:
        conn.close()
        return jsonify({"erro": "Autor não encontrado"}), 404

    conn.execute(
        "UPDATE autores SET nome = ?, nacionalidade = ? WHERE id = ?",
        (nome, nacionalidade, autor_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"id": autor_id, "nome": nome, "nacionalidade": nacionalidade})


@app.route("/autores/<int:autor_id>", methods=["DELETE"])
def apagar_autor(autor_id):
    conn = get_conn()
    autor = conn.execute("SELECT * FROM autores WHERE id = ?", (autor_id,)).fetchone()
    if autor is None:
        conn.close()
        return jsonify({"erro": "Autor não encontrado"}), 404

    conn.execute("DELETE FROM autores WHERE id = ?", (autor_id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Autor (e seus livros) apagado com sucesso"})

# CRUD - livros (tabela filho)

@app.route("/livros", methods=["GET"])
def listar_livros():
    conn = get_conn()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()
    return jsonify([dict(l) for l in livros])


@app.route("/livros/<int:livro_id>", methods=["GET"])
def buscar_livro(livro_id):
    conn = get_conn()
    livro = conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,)).fetchone()
    conn.close()

    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404

    return jsonify(dict(livro))


@app.route("/livros", methods=["POST"])
def criar_livro():
    dados = request.get_json(silent=True) or {}
    titulo = dados.get("titulo")
    ano_publicacao = dados.get("ano_publicacao")
    autor_id = dados.get("autor_id")

    if not titulo or not autor_id:
        return jsonify({"erro": "Os campos 'titulo' e 'autor_id' são obrigatórios"}), 400

    conn = get_conn()

    autor = conn.execute("SELECT id FROM autores WHERE id = ?", (autor_id,)).fetchone()
    if autor is None:
        conn.close()
        return jsonify({"erro": "Autor informado não existe"}), 400

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO livros (titulo, ano_publicacao, autor_id) VALUES (?, ?, ?)",
        (titulo, ano_publicacao, autor_id)
    )
    conn.commit()
    novo_id = cur.lastrowid
    conn.close()

    return jsonify({
        "id": novo_id,
        "titulo": titulo,
        "ano_publicacao": ano_publicacao,
        "autor_id": autor_id
    }), 201


@app.route("/livros/<int:livro_id>", methods=["PUT"])
def atualizar_livro(livro_id):
    dados = request.get_json(silent=True) or {}
    titulo = dados.get("titulo")
    ano_publicacao = dados.get("ano_publicacao")
    autor_id = dados.get("autor_id")

    if not titulo or not autor_id:
        return jsonify({"erro": "Os campos 'titulo' e 'autor_id' são obrigatórios"}), 400

    conn = get_conn()
    livro = conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,)).fetchone()
    if livro is None:
        conn.close()
        return jsonify({"erro": "Livro não encontrado"}), 404

    autor = conn.execute("SELECT id FROM autores WHERE id = ?", (autor_id,)).fetchone()
    if autor is None:
        conn.close()
        return jsonify({"erro": "Autor informado não existe"}), 400

    conn.execute(
        "UPDATE livros SET titulo = ?, ano_publicacao = ?, autor_id = ? WHERE id = ?",
        (titulo, ano_publicacao, autor_id, livro_id)
    )
    conn.commit()
    conn.close()

    return jsonify({
        "id": livro_id,
        "titulo": titulo,
        "ano_publicacao": ano_publicacao,
        "autor_id": autor_id
    })


@app.route("/livros/<int:livro_id>", methods=["DELETE"])
def apagar_livro(livro_id):
    conn = get_conn()
    livro = conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,)).fetchone()
    if livro is None:
        conn.close()
        return jsonify({"erro": "Livro não encontrado"}), 404

    conn.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Livro apagado com sucesso"})


# ROTAS ESPECIAIS (JOIN e filtros)

# JOIN: lista todos os livros com o nome do autor
@app.route("/livros-completo", methods=["GET"])
def listar_livros_completo():
    conn = get_conn()
    query = """
        SELECT livros.id, livros.titulo, livros.ano_publicacao,
               autores.id AS autor_id, autores.nome AS autor_nome
        FROM livros
        JOIN autores ON livros.autor_id = autores.id
    """
    resultado = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(r) for r in resultado])


# Filtro por caminho: todos os livros do autor especifico 
@app.route("/autores/<int:autor_id>/livros", methods=["GET"])
def listar_livros_do_autor(autor_id):
    conn = get_conn()

    autor = conn.execute("SELECT * FROM autores WHERE id = ?", (autor_id,)).fetchone()
    if autor is None:
        conn.close()
        return jsonify({"erro": "Autor não encontrado"}), 404

    livros = conn.execute(
        "SELECT * FROM livros WHERE autor_id = ?", (autor_id,)
    ).fetchall()
    conn.close()

    return jsonify([dict(l) for l in livros])


# Busca por query string com LIKE
@app.route("/livros/busca", methods=["GET"])
def buscar_livros_por_titulo():
    titulo = request.args.get("titulo", "")

    conn = get_conn()
    livros = conn.execute(
        "SELECT * FROM livros WHERE titulo LIKE ?", (f"%{titulo}%",)
    ).fetchall()
    conn.close()

    return jsonify([dict(l) for l in livros])


if __name__ == "__main__":
    init_db()
    app.run(debug=True)