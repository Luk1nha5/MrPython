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
            print("erro: salario não pode ser negativo sera definido 0.")
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