
flag_libro_barato=True
flag_libro_caro=True
menor_importe=0

porcentaje_ciencia=0
porcentaje_drama=0
porcentaje_terror=0
contador=0
contador_ciencia=0
contador_drama=0
contador_terror=0
contador_genero=0

acum_ciencia_ficcion=0

respuesta=input("usted realizo una compra de libro? si/no: ")
while (respuesta=="si"):
    contador+=1
    titulo=input("ingrese el titulo del libro: ")
    genero=input("ingrese el genero del libro (ciencia ficcion, drama, terror): ")
    while genero!= "ciencia ficcion" and genero!= "drama" and genero!= "terror":
        print ("genero invalido, vuelva a ingresarlo: ")
    material=input("ingrese el material del libro (rustica o tapadura): ")
    while material=="rustica" and material=="tapadura":
        print (f"su libro es de tapa: {material}")
    importe= int(input("ingrese el numero del importe: "))
    while (importe<0 and importe>30000):
        print("importe ingresado invalido, recuerde que no pueden ser numeros negativos, ni mayores a 30000: ")
if contador>1:
    respuesta=input("quiere seguir ingresando libros: si/no:  ")
    if (respuesta=="no"):
        print("proceso finalizado")


#a

if (genero=="drama"):
    if (flag_libro_barato==True):
        flag_libro_barato==False

        nombre_libro_barato=titulo
        menor_importe=importe
    elif (importe < menor_importe):
        menor_importe=importe
        nombre_libro_barato=titulo

    elif(flag_libro_caro==True):
        flag_libro_caro==False

        libro_caro=titulo

#b
porcentaje_ciencia=contador_ciencia*100/contador_genero
porcentaje_drama=contador_drama*100/contador_drama
porcentaje_terror=contador_terror*100/contador_terror

print (f"el porcentaje de ciencia ficcion es: {porcentaje_ciencia}, porcentaje de drama: {porcentaje_drama}, porcentaje de terror: {porcentaje_terror}")

#d
acum_ciencia_ficcion+=1

while (genero=="ciencia ficcion" and importe<700):
    print(f"la cantidad de libros de ciencia ficcion es: {acum_ciencia_ficcion}")