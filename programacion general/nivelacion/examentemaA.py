'''
Apple, Dunkin o Ikea.

● nombre
● edad (no menor a 18)
● está empleado (si-no)
● género (Masculino - Femenino - Otro)
● voto (APPLE, DUNKIN, IKEA)
Se necesita saber:
1. Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA,
cuya edad esté entre 25 y 50 años inclusive.
2. Nombre y voto del encuestado de género Masculino con menor edad.
3. Porcentaje de votos de cada género.
4. Promedio de edad de los encuestados de género Femenino que votaron
IKEA.
5. Determinar cuál fue el género que tuvo más encuestados
'''

respuesta="si"
contador=0
contador_no_empleados=0
contador_fem=0
contador_otro=0
contador_masculino=0
flag_menor_edad_masculino=True


respuesta=input("desea ingresar un voto: si /no  ")
while respuesta=="si":
    nombre=input("ingrese su nombre: ")
    edad=int(input("ingrese su edad, recuerde que debe ser no menor a 18: "))
    while edad<18:
        edad=int(input("ingrese su edad nuevamente: "))
    empleado=input("actualmente usted esta empleado? si/no ")
    while empleado!="si" and empleado!="no":
        empleado=input("ingrese una respuesta valida: ")
    genero=input("ingrese su genero (femenino/masculino/otro): ")
    while genero !="femenino" and genero!="masculino" and genero !="otro":
        genero=input("ingrese una de las opciones de genero dadas: ")
    voto=input("ingrese su voto: apple/ikea/dunkin:  ")
    while voto!="apple" and voto!="ikea" and voto!="dunkin":
        voto=input("ingrese un voto valido: ")

    contador+=1

    respuesta=input("desea continuar; si/no: ")
    if respuesta=="no":
        print("proceso finalizado")

    if (empleado=="no" and (voto=="dunkin" and voto =="ikea" and (edad>25 and edad>51))):
        contador_no_empleados+=1
    
    if (genero=="masculino"):
        contador_masculino+=1
        if (flag_menor_edad_masculino==True):
            flag_menor_edad_masculino=False
            nombre_menor_edad=nombre
            edad_menor=edad
            voto_menor=voto
        elif (edad<edad_menor):
            nombre_menor_edad=nombre
            edad_menor=edad
            voto_menor=voto
    elif(genero=="femenino"):
        contador_fem+=1
    elif (genero=="otro"):
        contador_otro+=1

    if (genero=="femenino" and voto=="ikea"):
        acum_edad_fem_ikea=edad

porcentaje_masculino=(contador_masculino/contador)*100
porcentaje_femenino=(contador_fem/contador)*100
porcentaje_otro=(contador_otro/contador)*100
promedio_femenino_ikea=acum_edad_fem_ikea/contador_fem

if (contador_masculino>contador_fem and contador_masculino>contador_otro):
    print("el genero mas encuestado fue: masculino")
elif (contador_fem>contador_masculino and contador_fem>contador_otro):
    print("el genero mas encuestado fue: femenino")
elif (contador_otro>contador_masculino and contador_otro>contador_fem):
    print ("el genero mas encuestado fue: otro")

print (f"la cantidad de desempleados es de {contador_no_empleados}")
print (f"el nombre del encuestado mas joven es {nombre_menor_edad} su voto es {voto_menor}")
print(f"porcentaje de votos femenino es {porcentaje_femenino}, masculino {porcentaje_masculino} y otros {porcentaje_otro}")
print(f"promedio de edad de mujeres que votaron ikea: {promedio_femenino_ikea}")

'''
3. Porcentaje de votos de cada género.
4. Promedio de edad de los encuestados de género Femenino que votaron
IKEA.
5. Determinar cuál fue el género que tuvo más encuestados
'''