def converter_para_inteiro(texto):
    try:
        numero = int(texto)
        return numero
    except ValueError:
        return "Conversão inválida."
    print(converter_para_inteiro("123"))
    print(converter_para_inteiro("abc"))