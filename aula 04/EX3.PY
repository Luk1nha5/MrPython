class contabancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("erro: o valor do deposito deve ser positivo")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("erro: saldo insuficiente para o saque")

    def get_saldo(self):
        return self.__saldo
    def extrato(self):
        print(f"titular: {self.__titular} saldo atual: {self.__saldo}")

conta = contabancaria("Mariana")
conta.depositar(100)
conta.sacar(40)
conta.sacar(80)
conta.extrato()