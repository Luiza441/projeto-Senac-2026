class ErroDeEntradaInvalida(Exception):
    pass

try:
    raise ErroDeEntradaInvalida("A entrada fornecida é inválida.")
except ErroDeEntradaInvalida as e:
    print(f"Erro capturado: {e}")
    