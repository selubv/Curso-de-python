ingreso_mensual = 81000
gasto_mensual = 74000

#if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien")
    else:
        print("Hay que ver si te alcansa")
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamérica")
elif ingreso_mensual > 500:
    print("Estas bien en Argentina")