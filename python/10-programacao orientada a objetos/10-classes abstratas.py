from abc import ABC, abstractmethod, abstractproperty  

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property    
    @abstractproperty    
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")

    def desligar(self):
        print("Desligando a TV...")

    @property
    def marca(self):
        return "Sony"     

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o AR...")

    def desligar(self):
        print("Desligando o Ar...")

    @property
    def marca(self):
        return "LG" 
             


controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

print("-" * 20)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)