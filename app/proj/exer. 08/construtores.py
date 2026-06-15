class Produto:
    def __init__(self, nome, preco):
        if preco <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")
        
        self.nome = nome
        self.preco = preco
        