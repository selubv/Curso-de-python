#Importando un módulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#desde ese modulo, importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar as saludar_normal, saludo_extraño as saludar_raro

#creamos las variables con los resultados
saludo = saludar_normal("Sergio")
saludo_raro = saludar_raro("Luis")

#mostramos los resultados
print(saludo)
print(saludo_raro)

#para ver las propiedades y los metodos del namespace
#print(dir(modulo_saludar))

#accedemos al nombre de este modulo
#print(__name__)

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)