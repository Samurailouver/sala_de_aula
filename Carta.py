class Carta:
    remetente: str
    conteúdo: str
    destinatario: str



    def __init__(self, remetente:str, conteúdo:str, destinario:str):
        self.remetente = remetente  
        self.conteúdo = conteúdo
        self.destinatario = destinario




#instancia

carta = Carta('João', 'Pyetra', 'Teamo ❤️')
