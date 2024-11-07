respuesta="si"
flag_alimento_mas_caro=True
contador_general=0
precioxkilo_vegetal=0
precioxkilo_animal=0
precioxkilo_mezcla=0
contador_vegetal=0
contador_animal=0
contador_mezcla=0
acum_preciovegetal=0


respuesta= input("desea que ingresemos los datos de la compra:  (si/no) ")
while (respuesta=="si"):
    peso=float(input("ingrese el peso en kilos: "))
    while peso<9 and peso >1001:
        print ("el peso ingresado no corresponde, ingrese un peso entre 9 y 1000")
        peso=float(input("ingrese el peso en kilos: "))
    precio_por_kilo= float(input("ingrese el precio por kilo: "))
    while precio_por_kilo<0:
        print("el precio por kilo ingresado no es valido, recuerde que debe ser mayor a 0")
    tipo_validado=input("ingrese el tipo de validacion: v o vegetal, a o animal o m o mezcla: ")
    while not (tipo_validado == "a" or "animal" and tipo_validado=="v" or "vegetal" and tipo_validado=="m" or "mezcla"):
        print ("el tipo de validado no es correcto, vuelva a ingresarlo: ")
contador_general+=1
print(respuesta=input("desea seguir ingresando datos:"))
if (respuesta=="no"):
    print ("proceso finalizado")

#a
if peso> 99 and peso <300:
    descuento=0.15
elif peso>300:
    descuento=0.25

total_a_pagar= peso*precio_por_kilo
total_con_descuento= total_a_pagar*descuento
print (f"el ttoal en bruto sin descuentos es {total_a_pagar} pesos.")
print (f"el total a pagar con descuentos incluidos es {total_con_descuento} pesos.")
#d
if (flag_alimento_mas_caro==True):
    nombre_alimento_mas_caro=tipo_validado
    precio_alimento_mas_caro=precio_por_kilo

#)Informar el tipo de alimento más caro.	

tipo_alimento_mas_caro="animal"
if (precioxkilo_mezcla>precioxkilo_vegetal and precioxkilo_mezcla>precioxkilo_animal):
    tipo_alimento_mas_caro="mezcla"
elif (precioxkilo_vegetal>precioxkilo_animal):
    tipo_alimento_mas_caro="vegetal"
print (f"el genero con mas encuestados fue {tipo_alimento_mas_caro}")


#el promedio de precio por kilo en total

if (contador_general!=0):
    precioxkilo_total=precioxkilo_animal+precioxkilo_mezcla+precioxkilo_vegetal
    promedio = precioxkilo_total/tipo_validado
    print (f"promedio de precio por kilo en total")