respuesta = "si"
flag_barbijo = True
flag_unidades = True
acum_unidades_jabon = 0
acum_unidades_barbijo = 0
acum_unidades_alcohol = 0
acum_unidades_gral = 0

while (respuesta == "si"):
    tipo = input("Tipo: ")
    while (tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        print("INVALIDO")
        tipo = input("Tipo: ")

    precio = int(input("Precio: "))
    while (precio < 100 or precio > 300):
        print("INVALIDO")
        precio = int(input("Precio: "))

    unidades = int(input("Unidades: "))
    while (unidades < 1 or unidades > 1000):
        print("INVALIDO")
        unidades = int(input("Unidades: "))

    fabricante = input("Fabricante: ")
    marca = input("Marca: ")

    if (tipo == "barbijo"):
        acum_unidades_barbijo += unidades

        if (flag_barbijo == True):
            precio_barbijo_mas_caro = precio
            cant_unidades_barb_caro = unidades
            fabricante_barb_caro = fabricante

            flag_barbijo = False
        elif (precio > precio_barbijo_mas_caro):
            precio_barbijo_mas_caro = precio
            cant_unidades_barb_caro = unidades
            fabricante_barb_caro = fabricante
    elif (tipo == "jabon"): 
        acum_unidades_jabon += unidades
    else:
        acum_unidades_alcohol += unidades

    if (flag_unidades == True):
        flag_unidades = False

        cant_max_unidades = unidades
        cant_max_unidades_fabri = fabricante
    if (unidades > cant_max_unidades):
        cant_max_unidades = unidades
        cant_max_unidades_fabri = fabricante

    acum_unidades_gral += unidades

    respuesta = input("Desea ingresar otro producto? (si): ")

tipo_mas_comprado = "Jabon"
if (acum_unidades_alcohol > acum_unidades_barbijo and acum_unidades_alcohol > acum_unidades_jabon):
    tipo_mas_comprado = "Alcohol"
elif (acum_unidades_barbijo > acum_unidades_jabon):
    tipo_mas_comprado = "Barbijo"

unidades_totales = acum_unidades_alcohol + acum_unidades_barbijo + acum_unidades_jabon
porcentaje_barbijos = acum_unidades_barbijo * 100 / unidades_totales