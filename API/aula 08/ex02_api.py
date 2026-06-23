from flask import Flask
app = Flask(__name__)

@app.route('/')
def bem_vindo():
    return "Bem Vindo "

@app.route('/curso')
def nome_curso():
    return "Desenvolvimento de Sistemas"

@app.route('/escola')
def nome_escola():
    return "CEEP" 

if __name__ == '__main__':
    app.run(debug=True)