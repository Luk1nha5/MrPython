from flask import Flask
from datetime import date
app = Flask(__name__)

@app.route('/saudacao')
def saudacao():
    return "bem vindo"

@app.route('/data')
def data_atual():
    hoje = date.today()

    data_formatada = hoje.strftime('%d/%m/%Y')
    return f"a data de hoje é: {data_formatada}"

if __name__ == '__main__':
    app.run(debug=True)