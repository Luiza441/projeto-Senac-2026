class Livro: 
    def __init__(self, titulo:str, autor:str, quantidade_copias:int):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_copias = int(quantidade_copias)

    def vender(self):
        if self.quantidade_copias > 0:
            self.quantidade_copias -= 1
            print(f"Uma cópia de '{self.titulo}' foi vendida!")
        else:
            print(f"Desculpe, o livro '{self.titulo}' está esgotado") 
    
    def reabastecer(self, quantidade):
        self.quantidade_copias += quantidade
        print(f"Estoque reabastecido! Agora existem \
            {self.quantidade_copias} cópias de '{self.titulo}'.")