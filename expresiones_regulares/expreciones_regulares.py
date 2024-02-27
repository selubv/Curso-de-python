import re

texto = """Hola maestro, esta es la cadena 1, como estas mi capitan
Esta es la linea 2 del texto
y esta es la final (linea 3) definitiva mi capitan"""

#Haciendo una busqueda simple de la primera coincidencia
#resultado = re.search("Esta", texto)

#Haciendo una busqueda simple de todas las coincidencias
#resultado = re.findall("Esta", texto)

#\d -> busca digitos numericos del 0 - 9
#resultado = re.findall(r"\d", texto)

#\D -> busca TODO menos digitos numericos del 0 - 9
resultado = re.findall(r"\D", texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w", texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W", texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\s", texto)

#\S -> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\S", texto)

#. -> busca TODO MENOS saltos de linea
resultado = re.findall(r".", texto)

#. -> busca saltos de linea
resultado = re.findall(r"\n", texto)

#\ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r'\.', texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(f'\d\.\s', texto)

#^ -> busca el comienzo de una linea (buscando hola al principio de la linea)
#flags=re.M activa la multilinea
resultado = re.findall(r'^Esta', texto, flags=re.M)

#$ -> busca el final de una linea
resultado = re.findall(r'capitan$', texto, flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda (3 numeros juntos esta vez)
resultado = re.findall(r'\d{3}', texto)

#{n,m} -> al menos n, como màximo m
resultado = re.findall(r'\d{2,4}', texto)

# | -> busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola', texto)

print(resultado)