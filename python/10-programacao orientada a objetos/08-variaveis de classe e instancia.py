class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero} - {self.escola})"

def mostrar_alunos(*objs):
    for obj in objs:
        print(obj)        

aluno_1 = Estudante("Danillo", 1)
aluno_2 = Estudante("Thais", 2)
mostrar_alunos(aluno_1, aluno_2)

print("-" * 25)

Estudante.escola = "Escola da Vida"
aluno_2.numero = 4
aluno_6 = Estudante("Raphaela", 6)
mostrar_alunos(aluno_1, aluno_2, aluno_6)