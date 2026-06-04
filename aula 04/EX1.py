class produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def set_nome(self, nome):
        self.__nome = nome
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("erro: preço não pode ser negativo")

prod = produto("caderno", 15.0)
prod.set_preco(-5)
prod.set_preco(12.5)
print(prod.get_nome(), "-", prod.get_preco())