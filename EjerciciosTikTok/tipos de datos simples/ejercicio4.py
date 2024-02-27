# Escribir un programa que lea un entero porsitivo,  n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros
# desde 1 hasta  n . La suma de los  n  primeros enteros positivos puede ser calculada de la siguiente forma:
# suma=n(n+1)/2

class SumaN:
    def __init__(self):
        self.numero = int(input("Ingrese un numero: "))

    def suma(self):
        self.sum = int(self.numero * (self.numero + 1) / 2)
        print(f"La suma de los enteros desde 1 hasta {self.numero} es: {self.sum}")

sumaNEnteros = SumaN()
sumaNEnteros.suma()