
def dividir_numeros(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero."
    print(dividir_numeros(10, 2))
    print(dividir_numeros(10, 0))