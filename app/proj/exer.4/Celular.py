from Celular import Dispositivo

class Celular(Dispositivo):
    def __init__(self, nome: str, bateria: int):
        super().__init__(nome)
        self.bateria = bateria