# API de Biblioteca

API REST desenvolvida em Python com Flask e banco de dados SQLite.

**Disciplina:** Programação no Desenvolvimento de Sistemas
**Dupla:** [Nome do integrante 1] e [Nome do integrante 2]

---

## 📋 Sobre o projeto

Este sistema controla o acervo de uma biblioteca: quem escreveu o quê. Cada autor pode ter vários livros cadastrados, e cada livro está sempre ligado a um autor. Além do CRUD básico (cadastrar, editar, apagar e consultar), dá pra ver os livros já com o nome do autor junto (sem precisar procurar o id manualmente) e filtrar tanto por autor quanto por parte do título do livro.

---

## 🗂️ Tabelas do banco

### Tabela `autores` (pai)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (gerada automaticamente) |
| nome | TEXT | Nome do autor (obrigatório) |
| nacionalidade | TEXT | Nacionalidade do autor |

### Tabela `livros` (filho)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (gerada automaticamente) |
| titulo | TEXT | Título do livro (obrigatório) |
| ano_publicacao | INTEGER | Ano em que o livro foi publicado |
| autor_id | INTEGER | Chave estrangeira → aponta para `autores.id` |

**Relação:** um autor → vários livros (1:N). Na tabela `livros`, o campo `autor_id` é uma FOREIGN KEY criada com `ON DELETE CASCADE`: se um autor for apagado, todos os livros associados a ele somem junto automaticamente, sem deixar "livro órfão" no banco.

---

## 🚀 Como rodar o projeto

```bash
# 1. Instalar o Flask (caso não tenha)
pip install flask

# 2. Rodar a API
python app.py

# 3. A API estará disponível em:
# http://127.0.0.1:5000
```

O banco de dados (`biblioteca.db`) é criado automaticamente na primeira execução.

---

## 🛣️ Rotas da API

### Tabela autores

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/autores` | Lista todos os autores |
| GET | `/autores/<id>` | Busca um autor pelo id |
| POST | `/autores` | Cria um novo autor |
| PUT | `/autores/<id>` | Atualiza um autor |
| DELETE | `/autores/<id>` | Apaga um autor (e seus livros, por causa do CASCADE) |

### Tabela livros

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/livros` | Lista todos os livros |
| GET | `/livros/<id>` | Busca um livro pelo id |
| POST | `/livros` | Cria um novo livro |
| PUT | `/livros/<id>` | Atualiza um livro |
| DELETE | `/livros/<id>` | Apaga um livro |

### Rotas especiais

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/livros-completo` | Lista livros já com o nome do autor (JOIN) |
| GET | `/autores-completo` | Lista autores com seus livros, inclusive os sem nenhum livro (LEFT JOIN – diferencial) |
| GET | `/autores/<id>/livros` | Lista os livros de um autor específico (filtro por caminho) |
| GET | `/livros/busca?titulo=x` | Busca livros por título, usando LIKE (filtro por query string) |

---

## 🧪 Como testar

Os testes estão no arquivo [`testes.http`](./testes.http).

Exemplo de requisição para criar um autor:

```http
POST http://127.0.0.1:5000/autores
Content-Type: application/json

{
    "nome": "Machado de Assis",
    "nacionalidade": "Brasileira"
}
```

---

## 👥 Integrantes

- [Nome 1] — [o que fez no projeto]
- [Nome 2] — [o que fez no projeto]
