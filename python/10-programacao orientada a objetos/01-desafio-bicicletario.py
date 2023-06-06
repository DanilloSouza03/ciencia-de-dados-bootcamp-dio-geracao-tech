class Bicicleta:
    def __init__(self, cor, marca, modelo, ano, valor):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim Plim...")
    
    def frear(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrum...")    
    
    def get_cor(self):
        return self.cor
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        

b1 = Bicicleta("branca", "caloi", "vulcan", 2023, 950)        

print(b1.cor, b1.marca, b1.modelo, b1.ano, b1.valor)

b1.buzinar()
b1.correr()
b1.frear()

b2 = Bicicleta("preta", "gallo", "Pro-G", 2023, 900)
print(b2)