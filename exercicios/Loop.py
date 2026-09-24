def dobrar(numeros:list):
    for numero in numeros:
        numero = numero * 2
        print(numero)

# Exercicio #1
def filtrar_pares(numeros:list):
    pares = [] # ou pares = list()
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    return pares

# Exercicio #2
def contar_negativos(numeros:list):
    count = 0
    for numero in numeros:
        if numero < 0:
            count+=1
    
    return count

#Exercicio #3
def soma_maiores_que(numeros:list, limite:int):
    soma = numeros.index()
    for numero in numeros:
        if numero > limite:
            soma+=numero

        return soma

#Exercicio #4
def zerar_negativos(numeros:list):
    aux = numeros.copy()
    for n in numeros:
        if n < 0:
         indice = numeros.index(aux)
         aux[indice]=0

    return aux



    
         

if __name__ == '__main__':
    
   
   
   
   
    numeros_pares = filtrar_pares([1, 2, 3, 4, 5, 6])
    print(numeros_pares)
    
    count = contar_negativos([3])
    print(count)

    soma = soma_maiores_que([45])
    print(soma)

    numeros_zerar = zerar_negativos([4, 0, 7, 0, 0])
    print(numeros_zerar)




