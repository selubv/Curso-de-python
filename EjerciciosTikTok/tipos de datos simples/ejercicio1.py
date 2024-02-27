# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena
# ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
class NombreUsuario:
    def __init__(self):
        self.nombre = None

    def obtener_nombre(self):
        self.nombre = input("Ingrese tu nombre: ")

    def saludar(self):
        print(f"¡Hola {self.nombre}!")

saludo = NombreUsuario()
saludo.obtener_nombre()
saludo.saludar()