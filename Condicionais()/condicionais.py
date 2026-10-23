# Exercicios 

def fizz_buzz(numero:float):
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizz"
    if numero % 5 == 0:
        return "buzz"
    elif numero % 3 == 0:
        return "fizzbuzz"
    else:
        return numero

# Exercicios 1

def verificar_maioridade(idade:float):
    if  idade > 18: 
        return "Maior de idade"
    if idade < 18:
        return "Menor de idade"

# Exercicios 2

def verificar_paridade(numero:float):
    if numero % 2 != 0:
        return "Impar" 
    else:
        return "Par"

# Exercicios 3

def classificar_numero(numero:float):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"

# Exercicios 4

def calcular_resultado(nota_1:float, nota_2:float): 
    if (nota_1 + nota_2) / 2 > 7:
        return "Aprovado"
    return "Reprovado" 

# Exercicio 5

def maior_de_dois(a:int, b:int):
    if a > b:
        return "O primeiro é maior" 
    if a < b:
        return "O segundo é maior"
    else:
        return "São iguais"

# Exercicio 6
# Se for Vip ou uma compra acima de 200.
# acima de 200 % 15 de desconto. Caso contrário 5% 
#retorne uma F-string com valor final.

def calcular_desconto( valor_da_compra:float, e_cliente_vip: float):
    resultado = valor_da_compra + e_cliente_vip
    resultado = e_cliente_vip - 15
    resultado = valor_da_compra - 5
    return f"Valor final:R${resultado}"

# Exercicio 7
# "A" = (10.0, 9.0), "B" = ( 8.0, 7.0), "C" = (5.0, 6.9), "F" = ( 5.0 )

def conceito_nota(nota:str):
    if nota == ("A" + "B") > 7.0:
        return "B"
    else:
        return "F"
    
if __name__ == "__main__":  
    
    teste = fizz_buzz(15)
    print(teste)
    idade = verificar_maioridade(20)
    idade = verificar_maioridade(15)
    print(idade)
    numero = verificar_paridade(7)
    numero = verificar_paridade(12)
    print(numero)
    numero = classificar_numero(0)
    numero = classificar_numero(-5)
    print(numero)
    calcular = calcular_resultado(8.0, 6.0)
    calcular = calcular_resultado(5.0, 6.5)
    print(calcular)
    maior = maior_de_dois(10, 20)
    maior = maior_de_dois(5, 5)
    print(maior)
    nota = conceito_nota(8.5)
    nota = conceito_nota (4.2)
    print(nota)
    valor = calcular_desconto(150.0, True)
    valor = calcular_desconto(100.0, False)
    print(valor)
