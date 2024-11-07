rta = "si"
flag_masc_men = 0
contador_desempleados = 0
menor_masc = 0
nombre_menor_masc = 0
voto_menor_masc = 0
edad_menor_masc = 0
contador_m = 0
contador_f = 0
contador_o = 0
contador = 0
acumulador_fem_pin = 0
edad_fem_pin = 0

while rta == "si":
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad (no menor a 18): "))
    while edad < 18:
        edad = int(input("Reingrese su edad (no menor a 18): "))
    empleado = input("Actualmente empleado si/no: ")
    while empleado != "si" and empleado != "no":
        empleado = input("Reingrese los datos. Empleado si/no: ")
    genero = input("Ingrese su genero m/f/o: ")
    while genero != "m" and genero != "f" and genero != "o":
        genero = input("Reingrese su genero m/f/o: ")
    voto = input("Ingrese su voto apple/dunkin/ikea: ")
    while voto != "apple" and voto != "dunkin" and voto != "ikea":
        voto = input("Reingrese su voto apple/dunkin/ikea: ")
    contador += 1
    rta = input("¿Desea seguir ingresando personas? si/no: ")

    if empleado == "no" and voto == "dunkin" or voto == "ikea" and edad >= 25 and edad <= 50:
        contador_desempleados += 1   

    if genero == "m": 
        contador_m += 1
        if flag_masc_men == 0:
            nombre_menor_masc = nombre
            voto_menor_masc = voto
            edad_menor_masc = edad
            flag_masc_men = 1
        elif edad < edad_menor_masc:
            nombre_menor_masc = nombre
            voto_menor_masc = voto
            edad_menor_masc = edad

    elif genero == "f":
        contador_f
        if voto == "ikea":
            edad_fem_pin += edad
            acumulador_fem_pin += 1
    else:
        contador_o

porcentaje_m = (contador_m / contador) * 100
porcentaje_f = (contador_f / contador) * 100
porcentaje_o = (contador_o / contador) * 100
promedio_fem =  (edad_fem_pin / acumulador_fem_pin)

if contador_m > contador_f and contador_m > contador_o: 
    print("El genero que tuvo mas encuestados fue el Masculino")
elif contador_f > contador_o:
    print("El genero que tuvo mas encuestados fue el Femenino")
else:
    print("El genero que tuvo mas encuestados fue el Otro")

print(f'''El promedio de edad de los encuestados Femenino que votaron por IKEA fueron {promedio_fem}''')
print(f'''El porcentaje de votos Masculinos fue: {porcentaje_m}, el porcentaje de votos Femeninos fue: {porcentaje_f}, y el porcentaje de votos Otro fue: {porcentaje_o}''')
print(f'''El nombre y voto del encuestado de genero masculino con menor edad fue: {nombre_menor_masc}, {voto_menor_masc}''')
print(f'''La cantidad de desempleados entre los 25 y 50 años que votaron por DUNKIN o IKEA fueron: {contador_desempleados}''')


'''
3. Porcentaje de votos de cada género.
4. Promedio de edad de los encuestados de género Femenino que votaron
IKEA.
5. Determinar cuál fue el género que tuvo más encuestados
'''