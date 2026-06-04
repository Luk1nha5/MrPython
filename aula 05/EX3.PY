class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def exibir(self):
        print(f"funcionario: {self.nome} salario base: {self.salario}")

class gerente(funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus 
    def salario_total(self):
        return self.salario + self.bonus

g = gerente("rodrigo", 53230.0, 4213210.0)
g.exibir()
print(f"salario total com bonus: {g.salario_total()}")