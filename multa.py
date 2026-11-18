# multa.py — o que a locadora cobra no balcão.
#
# Material da UC3, Aula 02. As regras abaixo foram escritas a partir do que o
# dono da locadora disse, e o código roda. Mas ninguém testou os casos da
# beirada: é isso que vocês vão fazer, antes de consertar qualquer coisa.
#
# As regras, nas palavras do dono:
#   - "Atrasou até 2 dias, eu perdoo. A partir do 3º dia de atraso, cobro
#     R$ 5,00 por dia de atraso — todos os dias, não só os que passaram de 2."
#   - "O aluguel é a diária vezes o número de dias. Ninguém aluga por zero
#     dias, nem por dias negativos: se pedirem isso, o sistema tem de recusar."

MULTA_POR_DIA = 5.00


def multa(dias_atraso):
    """Multa pela devolução atrasada, em reais."""
<<<<<<< HEAD
    if dias_atraso > 3:
=======
    if dias_atraso >= 3:
>>>>>>> aa71a02ab59703adb3b38176e4622f265c2b1cce
        return dias_atraso * MULTA_POR_DIA
    return 0.0


def valor_do_aluguel(diaria, dias):
    """Quanto o cliente paga ao retirar o jogo."""
<<<<<<< HEAD
=======
    if dias <= 0:
        raise ValueError('O número de dias não pode ser zero')
>>>>>>> aa71a02ab59703adb3b38176e4622f265c2b1cce
    return diaria * dias
