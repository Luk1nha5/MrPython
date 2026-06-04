class funcionario:
    def calcular_salario(self):
        return 0

class vendedor(funcionario):
    def __init__(self, fixo, comissao):
        self.fixo = fixo
        self.comissao = comissao
    def calcular_salario(self):
        return self.fixo + self.comissao
    
class gerente(funcionario):
    def __init__(self, fixo, bonus):
        self.fixo = fixo
        self.bonus = bonus
    def calcular_salario(self):
        return self.fixo + self.bonus
    
vendedor = vendedor(213131321.0, 5231.0)
gerente = gerente(1231232.0, 321321.0)

print(f"salario do vendedor: {vendedor.calcular_salario()}")
print(f"salario do gerente: {gerente.calcular_salario()}")