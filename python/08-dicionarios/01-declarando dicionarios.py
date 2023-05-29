pessoa = {"nome": "Danillo", "idade": 20}
print(pessoa)

pessoa = dict(nome="Danillo", idade=20)
print(pessoa)

pessoa["telefone"] = "3333-1234"  #{"nome": "Danillo", "idade": 20, "telefone": "3333-1234"}
print(pessoa)

print(pessoa["telefone"])
print(pessoa["nome"])
print(pessoa["idade"])