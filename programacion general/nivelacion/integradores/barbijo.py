
validar="si"
flag_barbijo_caro=0
cantidad_u_barbijo=0
fabricante_barbijo_caro=""
flag_unidades=0
max_unid=0
acumulador_u_jabon=0

while (validar=="si"):

    producto=input("que tipo de producto desea ingresar? ")
    while (tipo!="barbijo" or tipo!= "jabon" or tipo!="alcohol"):
        print ("el producto que ingreso no es valido, vuelva a intentarlo: ")
        tipo=input("que tipo de producto desea ingresar?: ")
    precio=int(input("ingrese el precio del producto, recuerde que debe ser entre el rango de 100 y 300: "))
    while (precio<100 or precio>300):
        print ("por favor ingrese un precio valido: ")
        precio =int(input("ingrese el precio del producto, recuerde que debe ser entre el rango de 100 y 300: "))
    cant_unidades=int(input("ingrese la cantidad de unidades (no menor a 0, no menor a 1000)"))
    while (cant_unidades<1 or cant_unidades>1000):
        print("por favor, ingrese la cantidad de unidades validas")
        cant_unidades=int(input("ingrese la cantidad de productos (no menor a 0, no menor a 1000)"))

    marca=input("ingrese la marca: ")

    fabricante=input("ingrese al fabricante: ")
    
    #A
    if (flag_barbijo_caro==0 and tipo=="barbijo"):
        precio_mas_caro_barbijo=precio
        cantidad_u_barbijo=cant_unidades
        fabricante_barbijo_caro=fabricante

        flag_barbijo_caro=1

    if (tipo=="barbijo" and precio>precio_mas_caro_barbijo):
        precio_mas_caro_barbijo=precio
        cantidad_u_barbijo=cant_unidades
        fabricante_barbijo_caro=fabricante
        
    #B
    if (flag_unidades==0):
        if (cant_unidades>max_unid):
            max_unid=cant_unidades
        fabricante_max_unidades=fabricante
        flag_unidades=1
    validar=int(input("desea seguir ingresando productos. escriba si para continuar o escriba no para finalizar"))
    #C unidades jabon
    acumulador_u_jabon+=1