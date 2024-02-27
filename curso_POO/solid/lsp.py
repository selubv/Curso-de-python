#este principio nos dice que la clase heredada debe hacer todo lo que la clase padre pueda hacer
class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        print("Estoy volando")

class AveNoVoladora(Ave):
    pass