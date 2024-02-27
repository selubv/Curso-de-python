class Persona:
    def __init__(self, nombre = None, fuerza = None, velocidad = None):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def crear_personaje(self):
        numero_personajes = int(input("Ingrese el numero de personajes a fusionar: "))
        personajes = []

        for p in range(numero_personajes):
            nombre = input(f"Ingrese el nombre del personaje {p}: ")
            fuerza = int(input(f"Ingrese la fuerza de {nombre}: "))
            velocidad = int(input(f"Ingrese la velocidad de {nombre}: "))
            personaje = Persona(nombre, fuerza, velocidad)
            personajes.append(personaje)

        return personajes

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza} Velocidad: {self.velocidad})"

    def __add__(self, otro_pj):
        nuevo_nombre = f"{self.nombre} - {otro_pj.nombre}"
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.5)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.5)
        return Persona(nuevo_nombre, nueva_fuerza, nueva_velocidad)

personaje = Persona()
fusion = personaje.crear_personaje()

personaje_fusionado = fusion[0]
for pj in fusion[1:]:
    personaje_fusionado += pj

print(personaje_fusionado)