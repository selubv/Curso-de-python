#                               Ejercicio 1
#a)Diferencia en porcentaje entre el curso actual y:
#1: El más rápido de otros cursos
t_curso_rapido = 2.5
t_curso_actual = 1.5
porc= 100

porcentaje = porc - ((100*t_curso_actual)/t_curso_rapido)

#2 El más lento de otros cursos
t_curso_lento = 7

porcentaje = porc - ((100*t_curso_actual)/t_curso_lento)

#3 El promedio de los cursos
t_promedio = 4

porcentaje = porc - ((100*t_curso_actual)/t_promedio)

#b) Porcentaje de material inservible que se reduce en:
#1. El promedio de los cursos
t_crudo = 5

porcentaje = porc - ((100*t_promedio)/t_crudo)

# 2. El curso actual (Este curso)
t_crudo_actual = 3.5

porcentaje = porc - ((100*t_curso_actual)/t_crudo_actual)

print(f'{porcentaje} %')

#c) Ver 10 horas de este curso a cuantas de otros cursos equivale? ¿y al revés?

promedio = 10*t_promedio/t_curso_actual

#d) y Al reves
promedio = 10*t_curso_actual/t_promedio

print(promedio)