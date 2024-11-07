precio=800
descuento=0

marca=input("ingrese la marca: ")
cantidad_lamparas= int(input("ingrese la cantidad de lamparas: "))


if (cantidad_lamparas>=6):
    descuento=0.50
elif (cantidad_lamparas==5):
    if (marca=="argentinaluz"):
        descuento=0.40
    else:
        descuento=0.30
elif (cantidad_lamparas==4):
    if(marca=="argentinaluz" or marca=="felipelamparas"):
        descuento=0.25
    else:
        descuento=0.20
elif (cantidad_lamparas==3):
    if (marca=="argentinaluz"):
        descuento=0.15
    elif (marca=="felipelamparas"):
        descuento=0.10
    else:
        descuento=0.5

descuento_adicional=0.5
precio_sin_descuento= cantidad_lamparas*precio
precio_con_descuento=precio_sin_descuento*descuento
descuento_adicional_total=0
if precio_con_descuento>4000:
    precio_con_descuento=precio_sin_descuento*(descuento-descuento_adicional)
    descuento_adicional_total=precio_sin_descuento*descuento_adicional
descuento_total= precio_sin_descuento- precio_con_descuento

print(f"La marca que eligio fue {marca}.")
print(f"la cantidad de lamparas que compra es {cantidad_lamparas}.")
if precio_con_descuento>4000:
    print(f"El descuento adicional realizado, debido a que el precio final supera los$4000, es de ${descuento_adicional_total}.")
print(f"El descuento total realizado fue de $ {descuento_total}.")
print(f"el precio de la compra, sin aplicarle ningun descuento, es de {precio_sin_descuento}")
print(f"el precio final de la compra es de ${precio_con_descuento}")

