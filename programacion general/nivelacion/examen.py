
respuesta="si"
contador_desempleados=0
contador_general=0

flag_masc_menor_edad=True
contador_femenino=0
acum_edad_femenino=0
contador_masculino=0
contador_otro=0
promedio_edad=0

porcentaje_femenino=0
porcentaje_masculino=0
porcentaje_otro=0

flag_masc_menor_edad=True

respuesta=input("desea ingresar un voto? si/no: ")
while respuesta=="si":
    contador_general+=1 #dsp de las validaciones
    nombre=input("ingrese su nombre: ")
    edad=int(input("ingrese su edad: "))
    while edad<18:
        edad=int(input("ingrese nuevamente su edad: "))
        
    empleado=input("usted es empleado (si/no): ")
    while empleado!="si" and empleado!="no":
        empleado=input("vuelva a ingresar su respuesta, usted es empleado? ")
    genero=input("ingrese su genero (masculino - femenino - otro):")
    while genero!="masculino" and genero !="femenino" and genero!= "otro":
        genero=input("ingrese su genero: ")
    voto=input("ingrese su voto: (APPLE, DUNKIN, IKEA): ")
    while voto!="APPLE" and voto!="DUNKIN" and voto!= "IKEA":
        voto=input("ingrese un voto de las opciones que correspondan: ")
    respuesta=input("desea seguir?: (si/no): ")
    if (respuesta=="no"):
        print ("proceso finalizado")

#poner dentro del bucle
if (empleado=="no" and (voto=="DUNKIN" and voto=="IKEA" and (edad>24 and edad<51))):
    contador_desempleados+=1

print(f"la cantidad de encuestado desempleados es de: {contador_desempleados}")


if (genero=="masculino"):
    if (flag_masc_menor_edad==True):

        nombre_menor_edad=nombre
        voto_menor_edad=voto
        menor_edad=edad

    flag_masc_menor_edad=False
    if (edad>menor_edad):
        nombre_menor_edad=nombre
        voto_menor_edad=voto
        #menor_edad=edad
    
print(f"el nombre y voto del genero masculino con menor edad es: {nombre_menor_edad} {voto_menor_edad}")


if (voto=="APPLE" and voto=="DUNKIN" and voto=="IKEA"):
    if(genero=="femenino"):
       porcentaje_femenino=contador_femenino*100/contador_general
    elif (genero=="masculino"):
       porcentaje_masculino=contador_masculino*100/contador_general
    elif(genero=="otro"):
       porcentaje_otro=contador_otro*100/contador_general
print(f"el porcentaje de votos de cada genero es; femenino:{porcentaje_femenino}, masculino: {porcentaje_masculino}, otro: {porcentaje_otro}")

if (contador_femenino!=0):
    if (genero=="femenino" and (voto=="IKEA")):
        promedio_edad=acum_edad_femenino/contador_femenino 
        print(f"promedio de edad de encuestados:femenino y voto por IKEA es de {promedio_edad}")
    else:
        print ("no se ingresaron mujeres")


genero_mas_encuestado="masculino"
if (contador_femenino>contador_masculino and contador_femenino>contador_otro):
    genero_mas_encuestado="femenino"
elif (contador_otro>contador_masculino and contador_otro>contador_femenino):
    genero_mas_encuestado="otro"

print(f"el genero que tuvo mas encuestados fue {genero_mas_encuestado}")

#prints   mal puestos


'''
Apple, Dunkin o Ikea.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
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
