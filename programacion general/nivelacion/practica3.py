'''
1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y
25 o entre 36 y 49 o que votaron por IKEA.
2. Nombre y género del encuestado de menor edad que votó por APPLE.
3. Porcentaje de encuestados de género Femenino que votaron por IKEA con
edad mayor a 25 años.
4. Edad promedio de los encuestados que están o no empleados (de cada
uno).
5. Determinar cuál fue la franquicia más votada. 
'''
respuesta="si"
contador=0
contador_masculino=0
contador_femenino=0
contador_femenino_ikea=0
contador_otro=0
contador_empleado=0
contador_no_empleado=0
contador_apple=0
contador_ikea=0
contador_dunkin=0
contador_caracteristico=0
flag_menor_edad_apple=True



respuesta=input("desea comenzar? si/no: ")
while respuesta=="si":
    nombre=input("ingrese su nombre: ")
    edad=int(input("ingrese su edad (no menor a 18): "))
    while edad<18:
        edad=int(input("ingrese su edad: "))
    empleado=input("actualmente es empleado? si/no ")
    while empleado!="si" and empleado !="no":
        empleado=input("ingrese una respuesta valida:  ")
    genero=input("ingrese un genero femenino/masculino/otro: ")
    while genero!="femenino" and genero !="masculino" and genero !="otro":
        genero=input("ingrese un genero valido: ")
    voto=input("ingrese su voto apple/dunkin/ikea: ")
    while voto !="apple" and voto !="dunkin" and voto !="ikea":
        voto=input("ingrese un voto valido: ")

    contador+=1
    respuesta=input("desea continuar? si/no: ")
    if respuesta=="no":
        print("proceso finalizado ")

    if (genero=="masculino"):
        contador_masculino+=1
        if (edad>18 and edad <25 or (edad>36 and edad <49 or (voto=="ikea"))):
            contador_caracteristico+=1
    elif (genero=="femenino"):
        contador_femenino+=1
        if (voto=="ikea" and (edad>25)):
            contador_femenino_ikea+=1
    elif (genero=="otro"):
        contador_otro+=1

    if (voto=="apple"):
        contador_apple+=1
        if (flag_menor_edad_apple==True):
            flag_menor_edad_apple=False
            nombre_menor_edad=nombre
            menor_edad=edad
            genero_menor_edad=genero
        elif(edad>menor_edad):
            nombre_menor_edad=nombre
            menor_edad=edad
            genero_menor_edad=genero
    elif (voto=="ikea"):
        contador_ikea+=1
    elif (voto=="dunkin"):
        contador_dunkin+=1

    if (empleado=="si"):
        contador_empleado+=1
    elif (empleado=="no"):
        contador_no_empleado+=1

promedio_empleados=contador_empleado/contador
promedio_no_empleados=contador_no_empleado/contador



if (genero=="femenino"):
    porcentaje_femenino_ikea=(contador_femenino_ikea/contador_femenino)*100
    print(f"el porcentaje femenino que voto por ikea es de {porcentaje_femenino_ikea}")
else:
    print("no se ingresaron mujeres") 
print (f"la cantidad de encuestado de genero masculino cuya edad va de 18 a 25 o de 36 a 49 o votaron a ikea es de {contador_caracteristico}")        
print (f"el nombre y genero del encuestado de menor edad que voto por apple es {nombre_menor_edad} y {genero_menor_edad}")
print(f"el promedio de edad de los empleados es de {promedio_empleados} y de los no empleados{promedio_no_empleados}")
if (contador_apple>contador_ikea and contador_apple>contador_dunkin):
    print("la franquicia mas votada fue apple")
elif (contador_dunkin>contador_apple and contador_dunkin>contador_ikea):
    print("la franquicia mas votadad fue dunkin")
elif (contador_ikea>contador_apple and contador_ikea>contador_dunkin):
    print("la franquicia mas votadad fue ikea")

