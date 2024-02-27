class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

nombre = input("Digame su nombre: ")
edad = input("Digite su edad: ")
grado = input("Que grado esta: ")

estudiante = Estudiante(nombre, edad, grado)

print(f'''
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      ''')

while True:
    estudiar = input("Escriba estudiar: ")
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()