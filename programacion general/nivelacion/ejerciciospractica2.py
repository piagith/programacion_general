

# 1. Porcentaje de votantes que realizaron el pago por mercado pago cuya edad es mayor a 50
# años (sobre el total de votantes).
# 2. El nombre del participante que recibió más votos.
# 3. Nombre y género del votante con más edad que votó a Bautista..
# 4. El promedio de edad de las votantes de otro género.
# 5. Cantidad de personas de género masculino o femenino, de más de 25 años que no
# votaron por Furia.


respuesta="si"
contador=0
contador_bautista=0
contador_emma=0
contador_otro=0
acum_edad_otro=0
contador_furia=0
contador_25_nofuria=0
flag_mas_edad=True
contador_mp=0
respuesta=input("desea votar?: si/no  ")
while respuesta=="si":
    nombre_votante=input("ingrese su nombre:")
    edad=int(input("ingrese su edad, debe ser mayor a 13 años para poder participar: "))
    while edad<13:
        edad=int(input("ingrese su edad nuevamente: "))
    genero= input("ingrese su genero (masculino/femenino/otro): ")
    while genero!="masculino" and genero!="femenino" and genero!="otro":
        genero=input("ingrese un genero valido: ")
    participante=input("ingrese el participante a quien quiere darle voto positivo; las opciones son Emma, Furia, Bautista: ")
    while participante!="Emma" and participante!="Furia" and participante!="Bautista":
        participante=input("ingrese una opcion correcta: ")
    medio_de_pago=input("realizo el pago con mercado pago: si/no  ")
    while medio_de_pago!="si" and medio_de_pago!="no":
        medio_de_pago=input("error, pago con mp? ")


    contador+=1
    respuesta=input("desea agregar otro voto? si/no")
    if respuesta=="no":
        print("fin")


    if edad>=50 and medio_de_pago=="si":
        contador_mp+=1

    if (participante=="Furia"):
        contador_furia+=1

    elif (participante=="Emma"):
        contador+=1
    elif (participante=="Bautista"):
        contador_bautista+=1
        if (flag_mas_edad==True):
            flag_mas_edad=False
            nombre_mas_edad=nombre_votante
            genero_mas_edad=genero
            edad_mayor=edad
        elif (edad>edad_mayor):
            nombre_mas_edad=nombre_votante
            genero_mas_edad=genero
            edad_mayor=edad
    if (genero=="otro"):
        contador_otro+=1
        acum_edad_otro+=edad

    if participante!="furia":
        if(edad>25 and (genero=="femenino" and genero=="masculino")):
            contador_25_nofuria+=1

porcentaje_Mp=(contador_mp/contador)*100
promedio_otro=acum_edad_otro/contador_otro
    
print(f"el porcentaje de votantes que ralizaron el pago por mercado pago cuya edad es mayor a 50 años {porcentaje_Mp}")
print (f"el nombre y genero del votante con mas edad que voto a bautista es {nombre_mas_edad} y {genero_mas_edad}")
if (contador_emma>contador_furia and contador_emma>contador_bautista):
    print ("el participante mas votado es Emma")
elif (contador_furia>contador_emma and contador_furia>contador_bautista):
    print ("el participante mas votado fue Furia")
elif (contador_bautista>contador_emma and contador_bautista>contador_furia):
    print ("el participante mas votado fue Bautista")
print (f"el promedio de edad de los votante de otro genero es de {promedio_otro}")

print (f"la cantidad de personas de genero masculino o femenio de mas de 25 años que no votaron por furia es de {contador_25_nofuria}")