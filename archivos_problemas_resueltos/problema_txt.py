#2 listas, una de nombres y otra de apellidos
nombres = ["Lucas", "Pedro", "Sergio", "Camilo"]
apellidos = ["Bonilla", "Dalto", "Zing", "Robetix"]

#Registrasr esta informacion en un txt de forma optima
with open("archivos_problemas_resueltos/nombres_apellidos.txt", "w", encoding="UTF-8") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n--------------\n") for n,a in zip(nombres,apellidos)]
