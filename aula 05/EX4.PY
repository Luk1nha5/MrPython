class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class aluno(pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    def apresentar(self):
        print(f"aluno: {self.nome} idade: {self.idade} matricula: {self.matricula}")

class professor(pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    def apresentar(self):
        print(f"professor: {self.nome} idade: {self.idade} salario: {self.salario}")

lista_pessoas = [
    aluno("Lucas", 16, "2312321"),
    professor("Diego", 34, 3211312.0),
    aluno("Beatriz", 17, "3211321")
]
for pessoa in lista_pessoas:
    pessoa.apresentar()