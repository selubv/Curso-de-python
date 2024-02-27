#creando un conjunto con set()
conjunto = set(["dato 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1, "dato 3"}

print(conjunto2)

#Teoria de Conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificamos si esa un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Verificamos si esa un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)