class Persona:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza} Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = f"{self.nombre} - {otro_pj.nombre}"
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.5)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.5)
        return Persona(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
goku = Persona("Goku", 100, 100)
vegetta = Persona("Vegeta", 99, 99)
giren = Persona("Giren", 130, 130)

gogeta = vegetta + goku
jireta = gogeta + vegetta

print(jireta)