from flask import Flask
from datetime import date  # Importando a dica do professor

app = Flask(__name__)

# Rota 1: Saudação
@app.route('/saudacao')
def saudacao():
    return "Seja muito bem-vindo à nossa API Flask!"

# Rota 2: Data de hoje
@app.route('/data')
def data_atual():
    hoje = date.today()
    # Formatando a data para o padrão brasileiro (DD/MM/AAAA)
    data_formatada = hoje.strftime('%d/%m/%Y')
    return f"A data de hoje é: {data_formatada}"

if __name__ == '__main__':
    app.run(debug=True)