def processar_dados(lista, indice):
    try:
        elemento = lista[indice]
        resultado = elemento / 2
        return resultado
    except IndexError:
        return "Erro: Índice fora dos limites da lista."
    except TypeError:
        return "Erro: O elemento encontrato não é um número."
          