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