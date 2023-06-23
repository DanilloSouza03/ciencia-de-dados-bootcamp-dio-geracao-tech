class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18   

# p = Pessoa("Danillo", 20)        
# print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(2003, 3, 25, "Danillo")        
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(5))
print(Pessoa.e_maior_idade(28))