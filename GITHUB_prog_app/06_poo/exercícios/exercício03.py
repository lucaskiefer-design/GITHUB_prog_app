#Contab Bancária

class ContaBancaria:
    def __init__(self, titular, novo_saldo, saldo_inicial = 0):
        self.titular = titular
        self.saldo_inicial = saldo_inicial
        self.novo_saldo = novo_saldo

    def depositar(self, valor):
        self.novo_saldo = self.saldo_inicial + valor

    def sacar(self, valor_saque):
        if self.novo_saldo < valor_saque:
            print("Saldo suficiente. Saque permitido")
        else:
            print("Saldo insuficiente. Saque negado")

    def extrato(self):
        print (f"Titular: {self.titular}")
        print(f"Saldo Atual: {self.novo_saldo}")

conta1 = ContaBancaria("Diel" , 0)
conta2 = ContaBancaria("Kurtz" , 0 , 500)


conta1.depositar(30)
conta1.sacar(400)
conta1.extrato()
print("\n")
conta2.depositar(30)
conta2.sacar(400)
conta2.extrato()