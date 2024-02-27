#Creando una lista con list()
lista = list(["hola", "sergio", 25, True])

#devuelve la cantidad de elementos de una lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("jajaja")

#agregando un elemento en un indice en especifico de una lista
lista.insert(2, "Holiiii")

#Agrega varios elementos a la lista
lista.extend([False, 23])

#elimina un elemento de la lista (por un indice)
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el antepenultimo ...

#removiendo un elemento de la lista por su valor
lista.remove("Hola")

#remover toda la lista
lista.clear()

#Ordena la lista de forma ascendente (Si usamos el parametro reverse = True lo ordena en reversa)
lista.sort()

#invierte los elementos de una lista
lista.reverse()

print(lista)