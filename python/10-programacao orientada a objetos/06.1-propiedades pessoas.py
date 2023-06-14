class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2023
        return _ano_atual - self._ano_nascimento  


pessoa = Pessoa("Danillo", 2003)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")