from relatorio import Aluguel, relatorioDoMes, test_total_de_alugueis_dos_clientes
def test_total_de_alugueis_dos_clientes():
    # Cenário
    alugueis = [
        Aluguel("Ana", "Fifa", 20)
        Aluguel("Bruno", "Zelda", 40.0),
        Aluguel("Carla", "Mario Kart", 25.0),      
    ]

    #Ação
    total = total_do_cliente(alugueis=alugueis, cliente="Ana")

    #Validação
    assert total == 65