class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamda desde tu: {self.modelo}")

celular1 = Celular("Samsung","S23", "48MP")
celular2 = Celular("Apple","Iphone 15 Pro", "96MP")

celular2.llamar()
