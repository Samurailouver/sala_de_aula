
# Exercicio 1
def formatar_saudacao(nome:str, cidade:str):
    return f"Olá {nome}, seja bem-vindo(a) a {cidade}!"

# Exercicio 2
def calcular_perimetro(largura: float, altura: float):
    perimetro = 2 * (largura+altura)
    return perimetro
# Exercicio 3
def fahrenheit_para_celsius(temp_f: float):
    celsius = (temp_f -32) * (5 / 9)
    return celsius    
# Exercicio 4
def calcular_gorjeta_por_pessoa(conta:float, porcentagem_gorjeta:float, pessoas:float):
    gorjeta = (conta * (porcentagem_gorjeta / 100)) / pessoas
    return gorjeta
# Exercicio 5
def resumo_circulo(raio: float):
    pi = 3.14159
    area = pi * (raio**2)
    return f"Um circulo com raio {raio} tem uma área de {area:.2f}"
# Exercicio 6
def resumo_juro_composto(capital:str , taxa:float ,anos: float):
    juros = capital * (1 + taxa / 100)**anos
    return f"Após 3 anos, R$ 1000.00 cresce para R${juros:.2f}."
# Exercicio 7
def metricas_cilindro(raio: float, altura: float):
    perimetro = altura 
    pi = 3.14159
    return f"Volume do Cilindro: 62.83 | Aréa de Superficie: {cilindro:.2f}"

if __name__ == '__main__':
    
    saudacao = formatar_saudacao("Alice","Porto Alegre")
    print(saudacao)
    perimetro = calcular_perimetro(5.0, 10.0)
    print(perimetro)
    celsius = fahrenheit_para_celsius(68)
    print(celsius)
    gorjeta = calcular_gorjeta_por_pessoa(100.0, 15, 3)
    print(gorjeta)
    area = resumo_circulo(3.0)
    print(area)
    juros = resumo_juro_composto(1000, 5.0, 3)
    print(juros)
    perimetro = metricas_cilindro(2.0, 5.0)
    print(perimetro)

    





