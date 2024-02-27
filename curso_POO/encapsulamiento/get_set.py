#declaramos la clase persona
class Persona:
    #definimos los atributos
    def __init__(self, nombre, edad):
        #definimos los atributos con _ para mostrar que son variables que no se pueden cambiar
        self._nombre = nombre
        self._edad = edad
    #el get es para mostrar atributos seguros
    def get_nombre(self):
        return self._nombre
    #el set se usa para modificar los valores del atributo seguro
    def set_nombre(self):
        self._nombre = new_nombre

dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()
print(nombre)