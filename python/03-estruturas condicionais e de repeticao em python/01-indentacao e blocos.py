def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor Sacado!")
    else:
        print("Saldo insuficiente!")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!!")     

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Seu saldo atual é de {saldo}.")


depositar(1000)