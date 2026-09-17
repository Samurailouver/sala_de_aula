# Exercicio

def fizz_buzz(numero:int):
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizz"
    if numero % 5 == 0:
        return "buzz"
    elif numero % 3 == 0:
        return "fizzbuzz"
    else:
        return numero

def verificar_maioridade(idade:float):
    if  idade > 18:
        return "Maior de idade"
    if idade < 18 :
        return "Menor de idade"

def verificar_paridade(numero:float):
    if numero % 2 != 0:
        return "Impar"  

    if __name__ == "__main__":  
    
        teste = fizz_buzz(15)
        print(teste)
        idade = verificar_maioridade(20)
        idade = verificar_maioridade(15)
        print(idade)
        numero = verificar_paridade(7)
        print(numero)
        
