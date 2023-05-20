nome = "Danillo"
idade = 20
profissao = "Cientista de Dados"
linguagem = "Python" 

#old style %
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
#f-string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159

print(f"O valor de PI: {PI:.2f}")
print(f"O valor de PI: {PI:10.2f}")