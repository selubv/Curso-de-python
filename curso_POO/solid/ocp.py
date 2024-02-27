#Este método nos indica que cada clase no deve se ser modificada solo agregar funciones para que sea más escalable y limpio el código
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificador(self):
        print(f"Enviando mensaje por Email a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificador(self):
        print(f"Enviando mensaje a {self.usuario.sms}")
