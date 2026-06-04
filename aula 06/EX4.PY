class pagamento:
    def processar(self, valor):
        return valor

class dinheiro(pagamento):
    def processar(self, valor):
        return valor * 0.95

class cartao(pagamento):
    def processar(self, valor):
        return valor * 1.02

class pix(pagamento):
    def processar(self, valor):
        return valor

formas_pagamento = [dinheiro(), cartao(), pix()]
valor_compra = 100.0
for forma in formas_pagamento:

    nome_forma = forma.__class__.__name__
    valor_final = forma.processar(valor_compra)
    print(f"pagamento: {nome_forma} {valor_final:.2f}")