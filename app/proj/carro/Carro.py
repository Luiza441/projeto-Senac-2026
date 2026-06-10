class Carro:
    def __init__(self, modelo: str, ano: int):
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def viajar(self, distancia: float):
        if distancia > 0:
            self.odometro   += distancia
            print(f"Viagem de {distancia} km realizada com sucesso!")
        else:
            print("Aviso: A disância da viagem deve ser um número positivo")