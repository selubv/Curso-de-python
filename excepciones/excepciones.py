#creando una funcion que suma numeros
def suma_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("Ingresa el numero 1: ")
        b = input("Ingresa el numero 2: ")
        #Intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
            #si lanzo una excepcion, pedirle que reingrese los datos
        except Exception as e:
            print("Te pedi un numero, no te hagas el gracioso")
            print(f'Error: {e}')
            #si todo salio bien terminamos el bucle
        else:
            break
        #finally se ejecuta siempre
        finally:
            print("Esto se ejecuta siempre")
    #mostramos el resultado
    return resultado
print(suma_dos())