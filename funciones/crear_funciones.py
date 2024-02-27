#creando una funcion simple
#def saludar():
#    print("hola papi, ¿Cómo estas?")

#ejecutando la funcion
#saludar()

#crear una funcion que tenga parametros
def saludar(nombre, genero):
    genero = genero.lower()
    if(genero == "mujer"):
        adjetivo = "señorita"
    elif (genero == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "pendejo"
    print(f"Hola {nombre}, mi {adjetivo} ¿Cómo estás?")

saludar("Camila", "Mujer")
saludar("Sergio", "Hombre")
saludar("Fran", "no binario")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_string = str(num)
    num = int(num_string[0])
    char1 = chars[num-2]
    char2 = chars[num]
    char3 = chars[num-5]
    contraseña = f'{chars[char1]}{chars[char2]}{chars[char3]}{num*2}'
    
    return contraseña, num

#desempaquetando la funcion
password, primer_num = crear_contraseña_random(981)

#mostrando los resultados optenidos y los datos utilizados para obtenerlos
print(f'Tu contraseña nueva es: {password}')
print(f'El número creada para utilizarla fue: {primer_num}')