palabra = input("Escribe algo: ")

cantidad_p = palabra.split(" ")

n_palabras = len(cantidad_p)

tiempo = n_palabras / 2 / 60
print(f'Dijiste {n_palabras} palabras')
print(f'Demoraste {tiempo} minutos')

if tiempo > 1 :
    print("para flaco tampoco te pedì un testamento")

tiempo_dalto = (n_palabras / 2 / 60)*0.7
print(f'Dalto lo diria en: {tiempo_dalto}')
