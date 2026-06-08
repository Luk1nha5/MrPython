class pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade
    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            print("erro: nome não pode ser vazio")

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else:
            print("erro: idade invalida")

    def apresentar(self):
        print(f"nome: {self.__nome} idade: {self.__idade}")

p = pessoa("Carlos", 20)
p.set_idade(150)
p.set_idade(25)
p.apresentar()