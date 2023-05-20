nome = "daniLlo"
#Normal
print(nome)
#Maiúscula
print(nome.upper())
#Minúscula
print(nome.lower())
#Título
print(nome.title())

nome_espaco = " danillo  "
#Normal
print(nome_espaco + ".")
#Remove espaço em branco
print(nome_espaco.strip() + ".")
#Remove espaço em branco esquerda
print(nome_espaco.lstrip() + ".")
#Remove espaço em branco direita
print(nome_espaco.rstrip() + ".")

menu = "Python"
#Normal
print(f"####{menu}####")
#Centralizar (1° argumento quantidade de caracteres e 2° o caracter que vai preencher)
print(menu.center(14, "#"))
#Junção
print("-".join(menu))