with open("archivos/txt", "w", encoding="utf-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("jajajaj holiiiiii")
    archivo.writelines(["Hola papu \n", "que tal"])