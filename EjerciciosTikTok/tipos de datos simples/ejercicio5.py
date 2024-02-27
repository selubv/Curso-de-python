#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m>
#son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

class Divisor:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def cociente_resto(self):
        cociente = self.n // self.m
        resto = self.n % self.m
        return cociente, resto

class InterfazUsuario:
    def obtener_numeros():
        n = int(input("Digite el primer numero: "))
        m = int(input("Digite el segundo numero: "))

        return n,m

    def mostrar_resultado(n, m, cociente, resto):
        print(f"{n} entre {m} da un cociente {cociente} y un resto {resto}")

n, m = InterfazUsuario.obtener_numeros()
divisor = Divisor(n, m)
cociente, resto = divisor.cociente_resto()
InterfazUsuario.mostrar_resultado(n, m, cociente, resto)

# class CocienteResto:
#     def __init__(self, n, m):
#         self.n = n
#         self.m = m

#     def numeros():
#         n = int(input("Digite el primer numero: "))
#         m = int(input("Digite el segundo numero: "))
#         return n,m

#     def cociente(n,m):
#         c = n // m
#         r = n % m
#         return c,r

# resultado = CocienteResto
# n,m = resultado.numeros()
# cociente, resto = resultado.cociente(n,m)

# print(f"{n} entre {m} da un cociente {cociente} y un resto {resto}")