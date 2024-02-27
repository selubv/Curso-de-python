#creando una lista (se puede cambiar)
lista = ["Sergio Bonilla", True, 1.62]

#creando una tupla (no se puede modificar)
tupla = ("Sergio Bonilla", True, 1.62)

#esto es válido
lista[2] = 1.70

#esto no
#tupla[2] = 1.70

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Sergio Bonilla", True, 1.62}

#print(conjunto[3]) -> no puede acceder al elemento

# creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Sergio Bonilla",
    'canal' : "Selubv",
    'esta_emocionado' : True,
    'altura' : 1.62,
    'dato_duplicado' : "Sergio Bonilla"
}

print(diccionario['altura'])
print(lista[3])