import pandas as pd

#cambiar el tipo de dato de una columna
df = pd.read_csv("archivos_problemas_resueltos/datos.csv")

#convertir a estring los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#reemplazando los datos dalto por "Maestro"
df['apellido'].replace("dalto", "maestro", implace=True)

#eliminando las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un csv con el dataframe resultante (limpio)
df.to_csv("archivos_problemas_resueltos/datos_limpios.csv")