class Aluno:
    def __init__(self, nome:str, notas:int):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def verificar_situaçao(self):
       media_atual = self.calcular_media()
       if media_atual >= 7.0:
           return "Aprovado"
       elif 5.0 <= media_atual < 7.0:
           return "Reprovado"
       