class forma:
    def area(self):
        return 0

class triangulo(forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

class quadrado(forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

formas = [triangulo(321, 123), quadrado(123), triangulo(1123, 312), quadrado(123)]
for forma in formas:
    print(f"Área da forma: {forma.area()}")