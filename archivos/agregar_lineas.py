with open("archivos/txt", 'a', encoding="UTF-8") as archivo:
    #usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        #agregar lineas
        archivo.write(f'Linea {i+1} lista: \n')