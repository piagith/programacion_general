contador_mascotas=0
contador_vacunaantirrabica=0
mascotas_problemas_digestivos=0
perro_problema=0
gato_problema=0
hamster_problema=0
contador_novacuna=0
acum_edad=0
contador_perro=0
flag_mascota_mas_vieja=True
contador_vacuna=0
fin=0

while(contador_mascotas<=15): 
    edad=int(input("ingrese la edad de su mascota: "))
    while (edad<1 or edad>21):
        edad=int(input("vuelva a ingresar la edad, debe estar entre 1 y 20 años: "))
    tipo=input("mascota: perro/gato/hamster:  ")
    while (tipo!="perro" and tipo !="gato" and tipo !="hamster"):
        tipo=input("ingrese una opcion valida: ")
    peso=int(input("ingrese el peso:  "))
    while (peso<=0):
        peso=int(input("ingrese un peso mayor a 0: "))
    diagnostico=input("ingrese una de las opciones: problemas digestivos/parasitos/infeccion:  ") 
    while (diagnostico!="problemas digestivos" and diagnostico!="parasitos" and diagnostico!="infeccion"):
        diagnostico=input("ingrese un diagnostico valido: ")
    vacuna=input("tiene vacuna antirrabica, si/no: ")
    while (vacuna!="si" and vacuna !="no"):
        vacuna=input("ingrese si / no: ")
    

    fin=input("usted desea finalizar? si/no : ")
    if (fin=="si"):
        contador_mascotas+=16
    contador_mascotas+=1
   
    if (vacuna=="si"):
        contador_vacuna+=1
        if (edad>=5 and edad<=10 and (diagnostico=="problemas digestivos" or diagnostico=="parasitos")):
            contador_vacunaantirrabica+=1  
            
            
    if (diagnostico=="problemas digestivos"):
        mascotas_problemas_digestivos+=1
        if (tipo=="perro"):
            perro_problema+=1
        elif (tipo=="gato"):
            gato_problema+=1
        elif (tipo=="hamster"):
            hamster_problema+=1
        
        
    if (vacuna=="no"):
        contador_novacuna+=1
        if (flag_mascota_mas_vieja==True):
            flag_mascota_mas_vieja=False
            tipo_mas_vieja=tipo
            diagnostico_mas_vieja=diagnostico
            edad_mas_vieja=edad
        elif (edad>edad_mas_vieja):
            tipo_mas_vieja=tipo
            diagnostico_mas_vieja=diagnostico
            edad_mas_vieja=edad

    if (tipo=="perro"):
        contador_perro+=1
        acum_edad+=edad


porcentaje_vacunasi=(contador_vacuna/contador_mascotas)*100
porcentaje_vacunano=(contador_novacuna/contador_mascotas)*100
promedio_edad_perro=acum_edad/contador_perro


if (perro_problema>gato_problema and perro_problema<hamster_problema):
    print ("el tipo de mascota con problemas digestivos es: perro")
elif (gato_problema>perro_problema and gato_problema>hamster_problema):
    print("el tipo de mascota con mas probkemas digestivos es: gato")
elif (hamster_problema>gato_problema and hamster_problema>perro_problema):
    print ("el tipo de mascota con problemas digestivos es: hamster")

print (f"la cantidad de mascotas con vacuna antirrabica cuya edad entre 5 y 10 años con problemas digestivos o parasitos es de {contador_vacunaantirrabica}")
print (f"la edad de la mascota mas vieja es {edad_mas_vieja} y el tipo es {tipo_mas_vieja} , sin vacuna antirrabica")
print (f"el porcentaje de mascotas vacunadas es de {porcentaje_vacunasi} y el porcentaje de las no vacunadas es de {porcentaje_vacunano}")
print (f"el promedio de edad de los perros es de {promedio_edad_perro}")
