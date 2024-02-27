class Calculadora:
    def calcular(self, a, b):
        raise NotImplementedError("Subclases deben implementar este método")
class Suma(Calculadora):
    def operacion(self, a, b):
        return a + b

class Resta(Calculadora):
    def operacion(self, a, b):
        return a - b

class Multiplicacion(Calculadora):
    def operacion(self, a, b):
        return a * b

class Division(Calculadora):
    def operacion(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        else:
            return a / b

# Ejemplo de uso
suma = Suma()
resta = Resta()
multiplicacion = Multiplicacion()
division = Division()

print(suma.operacion(5, 3))            # Salida: 8
print(resta.operacion(10, 4))          # Salida: 6
print(multiplicacion.operacion(2, 6))  # Salida: 12
print(division.operacion(10, 2))       # Salida: 5.0