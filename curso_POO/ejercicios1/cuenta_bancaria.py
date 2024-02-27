class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        
    def depositar(self, cantidad):
        self.saldo += cantidad
        
    def retirar(self, cantidad):
        if(self.saldo >= cantidad):
            self.saldo -= cantidad
        else:
            print("No cuentas con saldo suficiente")
            
    def obtener_saldo(self):
        return self.saldo
    
account = CuentaBancaria("123456", 1000)
print("Initial balance:", account.obtener_saldo())

account.depositar(500)
print("After deposit:", account.obtener_saldo())

withdrawn_amount = account.retirar(200)
print("Withdrawn amount:", withdrawn_amount)
print("After withdrawal:", account.obtener_saldo())