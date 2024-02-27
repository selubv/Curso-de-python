#si el modulo estubiera dentro de una carpeta en la misma ruta
#import funciones_buenas.saludar as m_saludar

import sys

#para ver las url de donde estamos
#print(sys.path)

sys.path.append("c:/home/selubv/Documentos/DATACRAFT/Curso de python/modulos")

import saludar as modulo_saludar

print(modulo_saludar.saludar("sergio"))