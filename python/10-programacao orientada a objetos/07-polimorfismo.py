class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# FIXME: exemplo ruim do uso de herança para "Ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()  
p2 = Avestruz()
a1 = Aviao()

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(a1)