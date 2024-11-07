''''


2. Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la
bolsa de valores:
De los inversionistas, no se sabe cuántos, registrar:
● Nombre
● Monto en pesos de la operación (no menor a $10000)
● Cantidad de instrumentos
● Tipo (CEDEAR, BONOS, MEP)
Calcular e informar:
a. Tipo de instrumento que más se operó.
b. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más
de $50000.
c. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que
menos dinero invirtió.
d. Porcentaje de usuarios que invirtiero
'''
respuesta="si"
contador=0
flag_libro_drama_barato=True
contador_drama=0
contador_ciencia_ficcion=0
contador_terror=0
flag_libro_caro=True
contador_700=0


respuesta=input("comenzamos?")
while respuesta=="si":
    titulo=input("ingrese el titulo: ")
    genero=input("ciencia ficcion/drama/terror: ")
    while genero !="ciencia ficcion" and genero !="drama" and genero !="terror":
      genero=input("ciencia ficcion/drama/terror: ")
    material=input("rustica/tapadura: ")
    while material !="rustica" and material !="tapadura":
      material=input("rustica/tapadura: ")
    importe=int(input("importe: "))
    while importe <0 and importe>30000:
       importe=int(input("importe: "))
    
    contador+=1
    respuesta=input("continuar: ")
    if respuesta=="no":
       print ("fin")

    if (genero=="drama"):
        contador_drama+=1
        if (flag_libro_drama_barato==True):
            flag_libro_drama_barato=False
            titulo_barato=titulo
            material_barato=material
            importe_barato=importe
        elif(importe>importe_barato):
            titulo_barato=titulo
            material_barato=material
            importe_barato=importe
    elif (genero=="ciencia ficcion"):
       contador_ciencia_ficcion+=1
    elif (genero=="terror"):
       contador_terror+=1
    
    if (flag_libro_caro==True):
       flag_libro_caro=False
       titulo_caro=titulo
       material_caro=material
       importe_caro=importe
    elif (importe<importe_caro):
       titulo_caro=titulo
       material_caro=material
       importe_caro=importe

    if (genero=="ciencia ficcion" and (importe<700)):
       contador_700+=1
       
porcentaje_cs_ficcion=(contador_ciencia_ficcion/contador)*100
porcentaje_terror=(contador_terror/contador)*100
porcentaje_drama=(contador_drama/contador)*100


print (f"el libro mas barato de drama con su importe es {titulo_barato} y su importe {importe_barato}")
print (f"el titulo del libro mas caro es: {titulo_caro}")
print (f"el porcentaje de libros de cada genero es {porcentaje_cs_ficcion} para cs ficcion, {porcentaje_drama} para drama, {porcentaje_terror} para terror.")
print (f"la cantidad de libros de cs ficcion y cuesten menos de 700 es de {contador_700}")

