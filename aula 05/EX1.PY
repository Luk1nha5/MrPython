class animal:
    def __init__(self, nome):
        self.nome = nome
    def comer(self):
        print(f"{self.nome} esta comendo")

class cachorro(animal):
    def latir(self):
        print(f"{self.nome} esta latindo Au Au")

meu_cachorro = cachorro("Bob")
meu_cachorro.comer()
meu_cachorro.latir()