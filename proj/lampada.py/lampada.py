class Lampada:
    def __init__(self):
        self.ligada = False

    def clicar_interruptor(self):
        self.ligada = not self.ligada

    def status(self):
        if self.ligada:
            return "a lâmpada está ligada"
        else:
            return "A lâmpada está desligada"
