<<<<<<< HEAD
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
        
=======
class RepositorioFalso:
    def __init__(self, emprestimos):
        self.emprestimos = emprestimos
        self.atualizados = []

    def abertos(self):
        return [e for e in self.emprestimos if e.data_entregue is None]

    def atualiza(self, emprestimo):
        self.atualizados.append(emprestimo)




    def test_avisa_quem_passou_do_prazo():
        atrasado = Emprestimo(1, "Ana Souza", "51 99999-0001", date(2026, 11, 1))

    cobrador = CobradorDeAtrasos()
    cobrador.cobrar()

    assert cobrador.total_avisados == 1
>>>>>>> aa71a02ab59703adb3b38176e4622f265c2b1cce
