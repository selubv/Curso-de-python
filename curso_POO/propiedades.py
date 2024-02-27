#creamos la clase persona
class Persona:
    #creamos el constructor asignando las variables
    def __init__(self, nombre, edad):
        #asignamos variables que no se pueden modificar __nombre
        self.__nombre =  nombre
        self._edad = edad

    #creamos el decorador @property para asignar un valor get
    @property
    def nombre(self):
        return self.__nombre

    #creamos el decorador @nombre.setter para poder modificar el valor set
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    #creamos el decorador @nombre.deleter para eliminar valores deleter
    @nombre.deleter
    def nombre(self):
        del self.__nombre

sergio = Persona("Luis", 25)

nombre = sergio.nombre
print(nombre)

sergio.nombre("Pepe")
nombre = sergio.nombre
print(nombre)

del sergio.nombre

nombre = sergio.nombre
print(nombre)
