from estoque import Livro

if __name__ == "__main__":
    Livro = Livro("Ensaio sobre a cegueira", "José Saramago", 4)
    Livro.vender()

    assert Livro.quantidade_copias
