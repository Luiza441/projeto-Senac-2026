class IdadeInvalidaError(Exception):
    pass

def cadastrar_eleitor(idade):
    if idade < 16:
        raise IdadeInvalidaError("A idade mínima para cadastro de eleitor é 16 anos.")
    
    print("Eleitor cadastrado com sucesso!")

