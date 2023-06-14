class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo        


conta = Conta("0001-04", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())

# conta._saldo += 100
# print(conta._saldo) 
# Não se deve fazer pois a variável está encapsulada, mesmo que dê "Certo" não é uma boa prática 