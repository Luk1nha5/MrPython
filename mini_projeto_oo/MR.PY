# =============================================
# SISTEMA DE FOLHA DE PAGAMENTO
# Mini Projeto - Orientação a Objetos
# =============================================


# --- CLASSE MÃE ---
# Aqui ficam os atributos que todos os funcionários têm em comum

class Funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        # Atributos privados (encapsulamento) - __ deixa o atributo privado
        self.__nome = nome
        self.__matricula = matricula
        # Uso o setter pra já validar o salário na criação do objeto
        self.set_salario_fixo(salario_fixo)

    # --- Getters ---
    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_salario_fixo(self):
        return self.__salario_fixo

    # --- Setters ---
    def set_nome(self, nome):
        self.__nome = nome

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_salario_fixo(self, salario_fixo):
        # Validação: não aceita salário negativo
        if salario_fixo < 0:
            print("Erro: salário não pode ser negativo! Será definido como 0.")
            self.__salario_fixo = 0
        else:
            self.__salario_fixo = salario_fixo

    # Método que cada filha vai sobrescrever com seu próprio cálculo (polimorfismo)
    def calcular_salario(self):
        pass

    # Exibe os dados do funcionário chamando o calcular_salario() de cada tipo
    def exibir(self):
        print(f"Nome : {self.__nome} | Matricula : {self.__matricula} | "
              f"Tipo : {type(self).__name__} | Salario : R$ {self.calcular_salario():.2f}")


# --- CLASSE FILHA: CLT ---
# Herda de Funcionario, salário = só o fixo

class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        # super() chama o __init__ da classe mãe
        super().__init__(nome, matricula, salario_fixo)

    # Polimorfismo: versão do CLT - só retorna o salário fixo
    def calcular_salario(self):
        return self.get_salario_fixo()


# --- CLASSE FILHA: Vendedor ---
# Herda de Funcionario, salário = fixo + 10% das vendas

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, total_vendas):
        super().__init__(nome, matricula, salario_fixo)
        # Atributo próprio do Vendedor
        self.__total_vendas = total_vendas

    def get_total_vendas(self):
        return self.__total_vendas

    def set_total_vendas(self, total_vendas):
        if total_vendas < 0:
            print("Erro: total de vendas não pode ser negativo!")
            self.__total_vendas = 0
        else:
            self.__total_vendas = total_vendas

    # Polimorfismo: versão do Vendedor - fixo + 10% de comissão
    def calcular_salario(self):
        comissao = self.__total_vendas * 0.10
        return self.get_salario_fixo() + comissao


# --- CLASSE FILHA: Gerente ---
# Herda de Funcionario, salário = fixo + bônus fixo de R$ 1500

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)
        # Bônus fixo pra todos os gerentes
        self.__bonus = 1500.00

    def get_bonus(self):
        return self.__bonus

    # Polimorfismo: versão do Gerente - fixo + bônus
    def calcular_salario(self):
        return self.get_salario_fixo() + self.__bonus


# =============================================
# PROGRAMA PRINCIPAL
# =============================================

# Criando um objeto de cada tipo
ana   = CLT("Ana", "001", 3000.00)
bruno = Vendedor("Bruno", "002", 2000.00, 12000.00)
carla = Gerente("Carla", "003", 5000.00)

# Colocando todos numa lista
funcionarios = [ana, bruno, carla]

# Percorrendo com for e chamando exibir() de cada um (polimorfismo em ação!)
print("===== FOLHA DE PAGAMENTO =====")
for funcionario in funcionarios:
    funcionario.exibir()
print("==============================")