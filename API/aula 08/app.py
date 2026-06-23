# Importa a classe Flask da biblioteca flask
from flask import Flask

1

# Cria a aplicacao
app = Flask(__name__)
# Define uma rota ( endereco ) para a raiz "/"
@app.route("/")
def inicio():
   return " Minha primeira API com Flask !"
# Roda o servidor
if __name__ == " __main__ ":
 app.run(debug=True)