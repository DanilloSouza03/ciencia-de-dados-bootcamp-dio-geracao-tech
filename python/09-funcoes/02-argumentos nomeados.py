def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Honda", "Civic", 1998, "ABC-1234")
salvar_carro(marca="Honda", modelo="Civic", ano=1998, placa="ABC-1234")
salvar_carro(**{"marca": "Honda", "modelo": "Civic", "ano": 1998, "placa": "ABC-1234"})
