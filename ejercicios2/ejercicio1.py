#falto el profesor y los alumnos van a armar la clase

#funcion para obtener al asistente y al profesor por edad
def obtener_compañero(cantidad):
    #creando la lista de los compañeros
    compañeros = []

    #ejecutando un for para pedir información de cada compañero
    for i in range(cantidad):
        nombre = input("Ingrese tu nombre: ")
        edad = input("Ingrese tu edad: ")
        compañero = (nombre, edad)

        #Agregamos la información a cada lista
        compañeros.append(compañero)

    #ordenamos de menor a mayor segun su edad
    compañeros.sort(key = lambda x : x[1])

    #compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    #retornamos una tupla
    return asistente, profesor

#desempaquetamos lo que nos retorna la funcion
asistente, profesor = obtener_compañero(5)

#mostrando el resultado
print(f'El profesor es: {profesor} y el asistente es: {asistente}')