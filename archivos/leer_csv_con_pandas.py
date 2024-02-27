import pandas as pd

#usando la funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos/datos.csv")
df2 = pd.read_csv("archivos/datos.csv")

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values(' edad')

#ordenandolo de forma descendente
df_orden_descendente = df.sort_values(' edad', ascending=False)

#concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 2 filas con head()
primeras_filas = df.head(2)

#accediendo a las ultimas 2 filas con tail()
ultimas_filas = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

#opteniendo data estadistica del dataframe
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico = df.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#Accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todos los apellidos con iloc
apellidos_iloc = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3_iloc = df.iloc[2,:]

#accediendo a filas con edad mayor a 30
mayor_30 = df.loc[df["edad"]>30,:]

print(df_concatenado)
