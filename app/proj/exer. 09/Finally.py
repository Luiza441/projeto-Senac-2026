def simular_banco_de_dados_(self, comando):
    try:
        print(f"Executando no banco: {comando}")
    except Exception as erro:
        print(f"Ocorreu um erro genérico: {erro}")
    finally:
        print("Conexão encerrada")