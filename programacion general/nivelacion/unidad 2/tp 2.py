#tp: reality

flag_votos= True
contador_jugadores=0
suma_edad=0
suma_votos=0

while (contador_jugadores<3):
    nombre = input("Nombre: ")
    
    edad= int(input("edad: "))
    while (edad<25):
          print ("edad invalida")
          edad=int(input("edad: "))

    votos=int(input("cant votos: "))
    while (votos<0):
         print ("invalida")
         votos=int(input("cant votos: "))
#nombre del candidato con mas votos

#nombre y edad del candidato con menos votos
    if (flag_votos):
        flag_votos=False
        votos_mayor = votos
        votos_menor=votos

        edad_votosmenor=edad
        nombre_votosmayor=nombre
        nombre_votosmenor=nombre

    if (votos>votos_mayor):
       votos_mayor=votos
       nombre_votosmayor=nombre
    elif(votos<votos_menor): 
       votos_menor=votos 
       nombre_votos_menor=nombre
#promedio edades
    suma_edad +=edad
 #total de votos emitidos
    suma_votos +=votos

    contador_jugadores += 1

promedio=suma_edad/contador_jugadores

msj =""
msj += (f"nombre del que mas votos tuvo {nombre_votosmayor}")
msj += (f"nombre del que menos votos tuvo: {nombre_votosmenor}")
msj +=(f"promedioo de edades: {promedio}")
msj +=(f"total votos emitidos: {suma_votos}")

print(msj)