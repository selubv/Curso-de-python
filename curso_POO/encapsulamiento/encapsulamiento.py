#definimos nuestra clase
class MiClase:
    #definimos un atributo encapsulado __atributo
    def __init__(self):
        self.__atributo_privado = "Valor"

    #definimos un metodo encapsulado __hablar()
    def __hablar(self):
        print("Hola, como estas")

objeto = MiClase()
#Saldra error porque los metodos encapsulados no se pueden acceder ni cambiar
print(objeto.__hablar())