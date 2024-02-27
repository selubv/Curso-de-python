frutas = ["manzana", "pera", "durazno", "Piña"]
texto = "Hola sergio"
numero = [1,5,9,3]

#evitando que se coma un durazno con la sentencia continue
for fruta in frutas:
    if fruta == "durazno":
        continue
    print(f"Me voy a comer la fruta {fruta}")

#evitar que el bucle s iga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer la fruta {fruta}")
    if fruta == "pera":
        break
else :
    print("terminado")

#recorrer una cadena de texto
for carac in texto:
    print(carac)

#for en una sola linea de código (duplicamos los numeros)
numeroDuplicado = [x*2 for x in numero]
print(numeroDuplicado)