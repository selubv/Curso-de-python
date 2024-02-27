#abriendo el archivo con with open
with open("archivos/txt", encoding="utf-8") as archivo:
    #leemos el archivo
    archivo =archivo.read()

    #mostramos el archivo
    print(archivo)

#no es necesario cerrarlo al usar with open