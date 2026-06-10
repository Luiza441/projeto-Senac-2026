class Termometro:
    def __init__(self, temperatura_atual:float):
        self.temperatura_atual = float(temperatura_atual)

        def aumentar(self, graus):
            self.temperatura_atual -= graus

        def alerta_clima(self):
            if self.temperatura_atual < 0:
                return "Congelando"
            elif 0 <= self.temperatura_atual <=25:
                return "Agradavél"
            else:
                return "Muito quente"