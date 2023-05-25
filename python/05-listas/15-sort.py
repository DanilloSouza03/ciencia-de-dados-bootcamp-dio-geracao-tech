nomes = ["Pedro", "Joao", "Carlos", "Juana", "Camila"]
nomes.sort()
#['Camila', 'Carlos', 'Joao', 'Juana', 'Pedro']  
print(nomes)

nomes = ["Pedro", "Joao", "Carlos", "Juana", "Camila"]
nomes.sort(reverse=True)  
#['Pedro', 'Juana', 'Joao', 'Carlos', 'Camila']
print(nomes)

nomes = ["Pedro", "Joao", "Carlos", "Juana", "Camila"]
nomes.sort(key=lambda x: len(x))  
#['Joao', 'Pedro', 'Juana', 'Carlos', 'Camila']
print(nomes)

nomes = ["Pedro", "Joao", "Carlos", "Juana", "Camila"]
nomes.sort(key=lambda x: len(x), reverse=True)  
#['Carlos', 'Camila', 'Pedro', 'Juana', 'Joao']
print(nomes)