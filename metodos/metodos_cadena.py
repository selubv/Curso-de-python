cadena1 = "Hola, Máquina, Como, Estas"
cadena2 = "Bienvenido Maquinola"

#Convierte a mayusculas
mayusc = cadena1.upper()

#Convierte a minusculas
minusc = cadena1.lower()

#Primera letra en mayuscula
primera_letra_mayusc = cadena1.capitalize()

#Buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("D")

#Buscamos una cadena en otra cadena, si no hay una coincidencia lanza una excepcion
busqueda_index = cadena1.index("D")

#si es numérico devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#Si es alfanumerico devuelve true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count(" la ma")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es así devuelve true
empieza_con = cadena1.startswith("Hola")

#Verifica si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("la")

#reemplaza un pedazo de una cadena por otra cadena dada
cadena_nueva = cadena1.replace("la", "lu")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada[0])