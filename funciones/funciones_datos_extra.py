#crando una funcion de tres parametros

#def frase(nombres, apellido, adjetivo):
#    return f'Hola {nombres} {apellido}, sos muy {adjetivo}'

#utilizando keyword arguments
#frase_resultante = frase(adjetivo = "capo", nombres = "sergio", apellido = "Bonilla")

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo = "tonto"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase("Lucas", "Dalto", "inteligente")
print(frase_resultante)