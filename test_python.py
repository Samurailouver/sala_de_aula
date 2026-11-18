class RepositorioFalso:
    def __init__(self):
        self.maior = "INF"
        self.menor = "INF"
        
    def avaliar(self, algueis):
        for aluguel in algueis:
            if aluguel.valor > self.maior:
                self.maior = aluguel.valor
            if aluguel.valor < self.menor:
                self.menor = aluguel.valor
                
        algueis = [
            aluguel("Ana", "FIFA 25", 30.0),
            aluguel("Bruno", "Zelda", 40.0),
            aluguel("Carlos", "Minecraft", 25.0)
        ]
        