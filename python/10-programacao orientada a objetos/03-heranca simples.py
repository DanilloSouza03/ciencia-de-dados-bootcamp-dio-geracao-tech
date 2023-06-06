class Veiculo:
    def __init__(self, cor, placa, numero_rodas, combustivel):
        self.cor = cor 
        self.placa = placa
        self.numero_rodas = numero_rodas
        self.combustivel = combustivel
    
    def ligar_motor(self):
        print("Ligando motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, combustivel, carregado):
        super().__init__(cor, placa, numero_rodas, combustivel,)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado.")    


moto = Motocicleta("vermelha", "abc-1234", 2, "gasolina")
carro = Carro("branco", "cba-4321", 4, "flex")
caminhao = Caminhao("azul", "bac-3241", 8, "diesel", True)

print(moto)
print(carro)
print(caminhao)