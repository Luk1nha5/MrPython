class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        valor_desconto = self.preco * (percentual / 100)
        novo_preco = self.preco - valor_desconto
        return novo_preco

meu_produto = produto("teclado", 250.0)
preco_com_desconto = meu_produto.desconto(10)

print(f"produto: {meu_produto.nome}")
print(f"preço original: {meu_produto.preco:.2f}")
print(f"preço com 10% de desconto: {preco_com_desconto:.2f}")