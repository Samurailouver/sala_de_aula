class RelatorioDoMes:
    
    def __init__(self):
       
        self.maior = float("-inf")   # começa no "menos infinito"
        self.menor = float("inf")    # começa no "mais infinito"


    def avaliar(self, alugueis):
        for aluguel in alugueis:
            if aluguel.valor > self.maior:
                self.maior = aluguel"valor"
            if aluguel.valor < self.menor:
                self.menor = aluguel"valor"
                alugueis = [

                Aluguel("Ana",   "FIFA 25",    30.0),
                Aluguel("Bruno", "Zelda",      40.0),
                Aluguel("Carla", "Mario Kart", 25.0),

]
                
relatorio = RelatorioDoMes()
relatorio.avaliar(alugueis)
print(relatorio.maior)   # 40.0
print(relatorio.menor)      #30.0