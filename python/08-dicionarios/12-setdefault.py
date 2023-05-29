contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna") 
print(contato)  #{'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28) 
print(contato)  #{'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
