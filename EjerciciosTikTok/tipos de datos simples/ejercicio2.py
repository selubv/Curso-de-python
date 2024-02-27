# Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que
# le corresponde.
class HorasTrabajadas:
    def __init__(self):
        self.horas = None
        self.coste = None

    def precio(self):
        self.horas = float(input("Ingrese horas de trabajo: "))
        self.coste = float(input("Ingrese lo que cobras por hora: "))

        paga = self.horas * self.coste
        print(f'La paga correspondiente es: {paga}')

# Crear una instancia de la clase y llamar al método precio
trabajo = HorasTrabajadas()
trabajo.precio()