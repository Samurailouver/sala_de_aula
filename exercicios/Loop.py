def dobrar(numeros:list):
    for numero in numeros:
        numero = numero * 2
        print(numero)

# Exercicio #1
def filtrar_pares(numeros:list):
    pares = numeros.copy()
    for numero in numeros:
        if numero % 2 != 0:
            pares.remove(numero)
        print(numero)

# Exercicio #2
def contar_negativos(numeros:list):
    negativos = []
    for numero in numeros:
        if numero > 0:
            negativos.append(numero)
            print(numero)

#Exercicio #3
def soma_maiores_que(numeros:list, limite:list):
    soma = []
    for numero in numeros


      

if __name__ == '__main__':
    
    dobrar([1,2,3,4,5]) 
    filtrar_pares([2, 4, 6])
    contar_negativos([3])
    soma_maiores_que([10 + 20 + 15])


