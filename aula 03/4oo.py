class banco:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f"depósito de {valor:.2f} realizado com sucesso")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"saque de {valor:.2f} realizado com sucesso")
        else:
            print("saldo insuficiente")

    def extrato(self):
        print("extrato")
        print(f"titular: {self.titular}")
        print(f"saldo atual: {self.saldo:.2f}")

conta = banco("Diógenes", 500.0)
conta.extrato()
conta.depositar(220) 
conta.sacar(145) 
conta.sacar(13000) 