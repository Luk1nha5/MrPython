class produto:
    def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco

produto1 = produto("notebook para fazer programa em python", 3500.0)
produto2 = produto("mouse top", 150.0)

print(f"produto 1: {produto1.nome} preço: {produto1.preco:.2f}")
print(f"produto 2: {produto2.nome} preço: {produto2.preco:.2f}")