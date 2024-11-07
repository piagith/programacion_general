



estudiante_mas_grande = float("inf")
total_sctividades = 0
genero_m = 'm'
genero_f = 'f'
genero_x = 'x'

total_edades = 0

ACTIVIDADES = ["futbol", "basket" , "voley", "natacion", "atletismo"]
contadores = [0, 0, 0, 0, 0]
contadores_de_genero = [0, 0, 0]

# lista pararela que nos sirve para contar cada actividad


while continuar == "s":
    nombre_completo = input ("ingrese su nombre completo")
    nombre_completo = validar_nombre(nombre_completo)

    edad = int(input("ingrese su edad: "))
    edad = validar_edad(edad)

    #contabilizar
    total_actividades += 1
    total_edades =

    # calcular el mayor
    if edad > estudiante_mas_grande:
        estudiante_mas_grande = nombre_completo
        estudiante_mas_grande = edad


    genero = input("ingrese su genero: ").lower()
    genero = validar_genero(genero)

    # aca depende del genro que indice contamos...
    match genero:
        case 'f':
            contadores_de_genero[0] += 1
        case 'm':
            contadores_de_genero[1] += 1
        case 'x':
            contadores_de_genero [2] += 2
    
    print("lista de actividades: ")
    print(ACTIVIDADES)
    eleccion_actividad = input ("inresa una actividad o Q para salir: ").lower()
    while eleccion_actividad != "q":
        for i in range(len(ACTIVIDADES)):
            if eleccion_actividad == ACTIVIDADES[i]:
                break

        eleccion_actividad = input ("¿desea agregar mas actividades (o ingrese Q para salir): ")

    continuar = input ("¿desea agregar mas estudiantes? s/n : ")
    if continuar != "s":
        continuar = False
        print ("hasta luego. ")


# una vez que salimos del while general tenemos que mostrar los analisis.
promedio =

#totoal por cada duna de las cactividades deberia ser ek otro contador (contadores)
for i in range (len(ACTIVIDADES)):
    print (f"el total de {ACTIVIDADES[i]} fue: {contadores[i]}")


#mostrar mayor estudiante
print (f"estudiante de mayor edad: {estudiante_mas_grande} su edad es: {estudiante_mas_grande}")
#el genero de mayor 
if contadores_de_genero [0] > contadores_de_genero[1] and contadores_de_genero [0]> contadores_de_genero[2]:
    mayor_genero = "femenino"
elif contadoress_de_genero [1] > contadores_de_genero [2]:
    mayoor_genero = "masculino"
else:
    mayor_genero = "no binario"
print (f"")