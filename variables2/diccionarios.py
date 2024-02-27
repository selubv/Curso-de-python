#creando diccionarios con dict()
diccionarios = dict(nombre="sergio", apellidos="Bonilla")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["sergio", "bonilla"]): "jajaja"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "nose"
diccionario = dict.fromkeys(["nombre", "apellidos"], "no se")

print(diccionario["nombre"])