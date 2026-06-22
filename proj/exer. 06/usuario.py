def validar_usuario(nome):
    if len(nome) < 3:
        raise ValueError("O nome deve ter pelo menos 3 caracteres.")
    return "Usuário válido"