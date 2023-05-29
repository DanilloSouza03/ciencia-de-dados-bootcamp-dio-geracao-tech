def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(17, 10, somar)  #O resultado da operação 17 + 10 = 27
exibir_resultado(17, 10, subtrair) #O resultado da operação 17 - 10 = 7

op = somar

print(op(10, 12)) #22