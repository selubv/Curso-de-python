class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola estoy hablando")
            
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola, soy: {self.nombre}, {self.habilidad} y trabaje en: {self.empresa}')
        
roberto = EmpleadoArtista("sergio", "25", "peruano", "Programar", "1k", "DataKraft")
roberto.presentarse()

#para ver si EmpleadoArtista es subclase de Persona
herencia = issubclass(EmpleadoArtista, Persona)

#identifica si Roberto es una instancia de Artista
instancia = isinstance(roberto, Artista)