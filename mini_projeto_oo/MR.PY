class funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        self.__nome = nome
        self.__matricula = matricula
        self.set_salario_fixo(salario_fixo)
 
    def get_nome(self):
        return self.__nome 
    def get_matricula(self):
        return self.__matricula
    def get_salario_fixo(self):
        return self.__salario_fixo

    def set_nome(self, nome):
        self.__nome = nome
    def set_matricula(self, matricula):
        self.__matricula = matricula
    def set_salario_fixo(self, salario_fixo):
        if salario_fixo < 0:
            print("erro: salario não pode ser negativo, vira 0.")
            self.__salario_fixo = 0
        else:
            self.__salario_fixo = salario_fixo
 
    def calcular_salario(self):
        pass
 
    def exibir(self):
        print(f"nome : {self.__nome} matricula : {self.__matricula} | "
              f"tipo : {type(self).__name__} salario : {self.calcular_salario():.2f}")

class CLT(funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)
    def calcular_salario(self):
        return self.get_salario_fixo()
    
class vendedor(funcionario):
    def __init__(self, nome, matricula, salario_fixo, total_vendas):
        super().__init__(nome, matricula, salario_fixo)
        self.__total_vendas = total_vendas
 
    def get_total_vendas(self):
        return self.__total_vendas
    def set_total_vendas(self, total_vendas):
        if total_vendas < 0:
            print("erro: total das vendas não pode ser negativo")
            self.__total_vendas = 0
        else:
            self.__total_vendas = total_vendas
 
    def calcular_salario(self):
        comissao = self.__total_vendas * 0.10
        return self.get_salario_fixo() + comissao
 
class gerente(funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)
        self.__bonus = 1500.00
 
    def get_bonus(self):
        return self.__bonus
    def calcular_salario(self):
        return self.get_salario_fixo() + self.__bonus

ana   = CLT("Ana", "001", 3000.00)
bruno = vendedor("Bruno", "002", 2000.00, 12000.00)
carla = gerente("Carla", "003", 5000.00)
 
funcionarios = [ana, bruno, carla]
for funcionario in funcionarios:
    funcionario.exibir()