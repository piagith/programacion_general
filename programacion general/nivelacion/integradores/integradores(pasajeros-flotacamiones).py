
Nombre_1= input("ingrese el nombre del primer pasajero: ")

Edad_1= int(input("ingrese la edad del primer pasajero: "))

Peso_1= float(input("ingrese el peso en kilos del primer pasajero: "))

#pasajero nro 2
Nombre_2= input("ingrse el nombre del segundo pasajero: ")

Edad_2= int(input("ingrese la edad del segundo pasajero: "))

Peso_2= float(input("ingrese el peso en kilos del segundo pasajero: "))

Costo_1_kilo= 1000
Total_viaje= Costo_1_kilo * (Peso_1+Peso_2)

Promedio_edad= (Edad_1 + Edad_2) / 2

Suma_peso= Peso_1 + Peso_2
print (f"Hola {Nombre_1} y {Nombre_2}, sus pesos son {Peso_1} y {Peso_2} kilos respectivamente, sumados da {Suma_peso} kilos, el promedio de edad es de {Promedio_edad} y su viaje cuesta en total {Total_viaje} pesos")


#empresa de camiones

cant_tonelads_materiales= float(input("ingrese cuanta cantidad de materiales en toneladas quiere transportar:  "))

peso_viaje_por_camion= 3.5
Cantidad_camiones= int(cant_tonelads_materiales / peso_viaje_por_camion)
print("cada camion puede transportar por viaje 3500 kilos, por ende, por la cantidad de toneladas de materiales ingresadas, que es :" ,cant_tonelads_materiales, "se necesitara" ,Cantidad_camiones, "camiones.") 

#B
kilometros= float(input("ingrese la cantidad de km de recorrido para llegar a destino: "))

velocidad = 90

tiempo=int(kilometros/velocidad)

print("el tiempo estimado de recorrido de los camiones es de", tiempo, "horas")