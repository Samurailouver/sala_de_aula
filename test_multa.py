from relatorio import RelatorioDoMes,Aluguel


def test_valor_por_dia():

    dias_atrasado = [
    
    Aluguel("Dia 2", 10),
    Aluguel("Dia 3", 15),
    Aluguel("Dia 4", 20),
    
    ]

    valores = sorted([a.valor for a in alugueis])
   