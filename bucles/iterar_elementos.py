animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [1, 5, 7, 10]

#rercorriendo la lista animales
for animal in animales:
    print(f'Este animal es: {animal}')

#recorriendo la lista de numeros duplicados
for num in numeros:
    result = num * 2
    print(f'El numero duplicado es: {result}')

#iterando dos listas del mismo tamaño al mismo tiempo
for animal, num in zip(animales, numeros):
    print(f'recorriendo la lista 1 : {animal}')
    print(f'recorriendo la lista 2 : {num}')

#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#usando el for else
for num in numeros:
    print(f"el valor es: {num}")
else:
    print("el bucle termino")

#todo lo anterios funciona igual con las tuplas y conjuntos.