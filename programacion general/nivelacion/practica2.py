'''
1. Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya
edad no supere los 36 años.
2. Nombre y voto del encuestado de género Femenino con mayor edad.
3. Porcentaje de encuestados de género Otro que votaron por DUNKIN.
4. Edad promedio de cada género.
5. Determinar cuál fue el género que tuvo menos encuestados
'''

respuesta="si"
contador=0
contador_empleados=0
contador_fem=0
contador_masculino=0
contador_otro=0
acum_edad_femenino=0
acum_edad_otro=0
acum_edad_masculino=0


flag_mayor_edad=True

respuesta=input("desea comenzar? si/no: ")
while respuesta=="si":
    nombre=input("ingrese su nombre: ")
    edad=int(input("ingrese su edad (no menores de 18 años): "))
    while edad <18:
        edad=int(input("ingrese su edad:  "))
    empleado=input("actualmente es empleado? si/no: ")
    while empleado!="si" and empleado!="no":
        empleado=input("ingrese una respuesta valida: ")
    genero=input("ingrese un genero (femenino/masculino/otro): ")
    while genero!="femenino" and genero!="masculino" and genero!="otro":
        genero=input("ingrese un genero valido: ")
    voto=input("ingrese su voto (apple/ikea/dunkin): ")
    while voto !="apple" and voto!="ikea" and voto !="dunkin":
        voto=input("ingrese su voto : ")
        
    contador+=1

    respuesta=input("desea continuar? si/no  ")
    if respuesta=="no":
        print("proceso finalizado ")

    if (empleado=="si" and (voto=="ikea" and voto=="apple" and (edad<36))):
        contador_empleados+=1
    
    if (genero=="femenino"):
        contador_fem+=1
        acum_edad_femenino=edad
        if (flag_mayor_edad==True):
            flag_mayor_edad=False
            nombre_mayor_edad=nombre
            mayor_edad=edad
            voto_mayor_edad=voto
        elif (edad<mayor_edad):
            nombre_mayor_edad=nombre
            mayor_edad=edad
            voto_mayor_edad=voto
    elif (genero=="masculino"):
        contador_masculino+=1
        acum_edad_masculino=edad
    elif (genero=="otro"):
        contador_otro+=1
        acum_edad_otro=edad
        if (voto=="dunkin"):
            contador_otro_dunkin=contador_otro

porcentaje_otro=(contador_otro_dunkin/contador)*100
promedio_femenino=acum_edad_femenino/contador_fem
promedio_masculino=acum_edad_masculino/contador_masculino
promedio_otro=acum_edad_otro/contador_otro


print (f"la cantidad de empleados, que votaron por ikea/apple, que no superan los 36 años es de {contador_empleados}")
print(f"el nombre de la persona genero femenino con mayor edad es {nombre_mayor_edad} y su voto fue {voto_mayor_edad}")
print (f"el porcentaje del genero otro que votaron por dunkin es de {porcentaje_otro}")
print (f"la edad promedio de cada genero es de {promedio_femenino} para el genero femenino, {promedio_masculino}para el masculino y para otros {promedio_otro}")
if (contador_fem<contador_masculino and contador_fem<contador_otro):
    print ("el genero menos encuestado fue el femenino")
elif (contador_masculino<contador_fem and contador_masculino<contador_otro):
    print("el genero menos encuestado fue el masculino")
elif (contador_otro<contador_fem and contador_otro<contador_masculino):
    print("el genero menos encuestado fue el genero otro")

