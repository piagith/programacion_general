respuesta="si"
flag_casado_masjoven=True
flag_mas_viejo_casado=True
suma_edad_hombres_soltero=True
suma_edad_mujeres=0
contador_hombres_sol=0
contador_mujeres=0
edad_casado_viejo=0
acum_mujeres_casadas=0
acum_mujeres_viudas=0
promedio_Edad_mujeres=0
promedio_Edad_hombres=0


respuesta=input("bienvenidos; desea ingresar pasajeros/as: (si/no) ")
while (respuesta=="si"):    
    nombre=input("ingrese su nombre: ")
    edad= int(input("ingrese su edad: "))
    while (edad<19):
        print("edad invalida, debe ser mayor de 18")
        edad=int(input("ingrese su edad nuevamente: "))
    sexo=input("ingrese su sexo (f/m):")
    while (sexo!= "f" and sexo!= "m"):
        print ("sexo invalido")
        sexo=print ("reingrese su sexo (f/m): ")
    estado_civil=input("ingrese su estado civil (soltero, casado o viudo)")
    while (estado_civil !="soltero" and estado_civil != "casado" and estado_civil != "viudo"):
        print ("estado civil invalido")
        estado_civil=input("reingrese su estado civil (soltero, casado o viudo)")       
    
    respuesta=input ("Desea seguir ingresando pasajeros/as?: (si/no)  ")
    if (respuesta=="no"):
        print("ok, hasta luego, proceso finalizado!")

#a) nombre del hombre casado mas joven.
if sexo=="m":
    if estado_civil=="casado":
        if (flag_casado_masjoven== True):
            nombre_casado_joven = nombre
            edad_casado_joven=edad

        flag_casado_masjoven=False
        if (edad > edad_casado_joven):
            nombre_casado_joven=nombre
            edad_casado_joven=edad

    elif estado_civil=="soltero":
        suma_edad_hombres_soltero +=edad
        contador_hombres_sol += 1
#b
if (flag_mas_viejo_casado==True):
    nombre_mas_viejo=nombre
    edad_mas_viejo=edad
    sexo_mas_viejo=sexo
flag_mas_viejo_casado=False
if (edad>edad_casado_viejo):
    nombre_Casado_viejo=nombre
    edad_casado_viejo=edad
    sexo_casado_viejo=sexo 

#c
elif sexo=="f":
    suma_edad_mujeres+=edad
    if estado_civil=="casado":
        acum_mujeres_casadas+=1
    elif estado_civil=="viudo":
        acum_mujeres_viudas +=1
    
contador_mujeres+=1


#d
promedio_Edad_mujeres=0
if contador_mujeres>0:
    promedio_Edad_mujeres=suma_edad_mujeres/contador_mujeres
#e
promedido_edad_hombres_Sol=0
if contador_hombres_sol:
    promedido_edad_hombres_Sol=suma_edad_hombres_soltero/contador_hombres_sol 

mensaje = f'''
el nombre del hombre casado mas joven es {nombre_casado_joven}
el pasajero/a mas grande se llama { nombre_mas_viejo} y su sexo es {sexo_mas_viejo}
la cantidad de mujeres casadas es {acum_mujeres_casadas} y viudas {acum_mujeres_viudas}
el promedio de edad entre mujeres es {promedio_Edad_mujeres}
el promedo de edad entre hombres solteros es de {promedido_edad_hombres_Sol}

'''
print(mensaje)

