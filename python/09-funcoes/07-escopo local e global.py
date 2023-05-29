salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_e_bonus = salario_bonus(500)  #2500
print(salario_e_bonus)