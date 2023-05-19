print("---inteiro para float---")
preco = 10
print(preco)
preco = float(preco)

print("---float para inteiro---")
preco = 10.30
print(preco)
preco = int(preco)
print(preco)

print("---conversão por divisão---")
preco = 10
print(preco)
print(preco / 2)
print(preco // 2)

print("---Númerico para String---")
preco = 10.50
idade = 25
print(str(preco))
print(str(idade))
texto = f"Idade {idade} preço {preco}"

print("---String para Númerico---")
preco = "10.50"
idade = "25"
print(float(preco))
print(int(idade))