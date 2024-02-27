diccionario = {
    "nombre" : 'sergio',
    "apellidos" : 'bonilla',
    "subs" : 53
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor = diccionario.get("qwe")
print("Holaaaa")

#eliminando todo del diccionario
diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterables
diccionario_iterable = diccionario.items()

print(diccionario_iterable)