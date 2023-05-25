#Filtrar lista sem comprehension
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#Filtrar lista com comprehension
numeros = [1, 30, 21, 2, 9, 65, 34]
impar = [numero for numero in numeros if numero % 2 != 0]
print(impar)

#Modificar valores com comprehension
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)