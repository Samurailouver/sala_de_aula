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

def calcular_desconto(valor_compra:float, e_cliente_vip:float):
    if e_cliente_vip / 15 < 200:
        return "valor final R$ 127.50"
    if valor_compra / 5 > 200:
        return "valor final R$ 95.00"
    
    
    
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
    calcular = calcular_desconto(150.0)
    calcular = calcular_desconto(100.0)
    print(calcular)