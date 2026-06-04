class veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
    def informacoes(self):
        print(f"marca: {self.marca} ano: {self.ano}")

class carro(veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

class moto(veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

meu_carro = carro("chevrolet", 1990, 4)
minha_moto = moto("honda", 2012, 160)

meu_carro.informacoes()
print(f"portas: {meu_carro.portas}")

minha_moto.informacoes()
print(f"cilindradas: {minha_moto.cilindradas}")