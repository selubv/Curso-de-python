#creando una funcion que nos devuelva los numeros primos entre 0 y el argumento que pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    #Verificamos que el numero que pasamos no pueda dividirse por ningun número entre 2 y ese mismo numero -1
    for i in range(2, num-1):
        #Si es divisible por alguno retornamos false y termina el bucle
        if num % i == 0: return False
    #Si termina el bucle, significa que no fue divisible entonces es primo
    return True

#Creando funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3, num+1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)

    #devolvemos la lista
    return primos

#creamos el resultado llamando a la funcion y lo mostramos
resultado = primos_hasta(98)
print(resultado)

#otra forma
primos_hastaa = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)),range(2, num)))

print(primos_hastaa(15))