flag_instrumento_operado=True
flag_usuario_menos_invirtio=True
porcentaje_mep=0
contador_mep=0

cantidad_instrumentos_inversion_min=0
contador_usuarios=0
acum_operadores=0
respuesta="si"
respuesta=input("desea operar? si/no :")
while (respuesta=="si"):
    contador_usuarios+=1

    nombre=input("ingrese su nombre: ")
    monto=float(input("ingrese el monto en pesos de la operacion: "))
    if (monto<10000):
        print ("monto ingresado invalido, recuerde que no debe ser menor a $10000")
    cantidad_instrumentos=int(input("ingrese la cantidad de instrumentos: "))

    tipo=input("ingrese el tipo de instrumento (cedear, bono, mep): ")
    while tipo!="cedear" and tipo!="bono" and tipo!="mep":
        print("ingrese un tipo valido: ")

    respuesta=input("desea seguir operando? si/no: ")
    if respuesta=="no":
        print ("programa finalizado")
        break
    elif respuesta!="si":
        print ("respuesta no valida, ingrese si o no")
        break

#a. Tipo de instrumento que más se operó.

if (flag_instrumento_operado==True):
    flag_instrumento_operado==False

    nombre_instrumento_operado=tipo

print (f"el instrumento mas operado fue: {nombre_instrumento_operado}")
    
# b. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.
 
if (tipo=="bono" and (cantidad_instrumentos>150 or cantidad_instrumentos<200)and (monto>50000)):
    contador_usuarios+=1
print (f"la cantidad de usuarios que compraron entre 150 y 200 bonos, con una inversion mayor a 50.000 es: {contador_usuarios}")

# c. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió.
if (tipo=="bonos" and tipo=="mep"):
    if (flag_usuario_menos_invirtio==True):
        flag_usuario_menos_invirtio=False
        
        nombre_menos_inversion=nombre
        cantidad_instrumentos_inversion_min=cantidad_instrumentos
        
    elif (cantidad_instrumentos<cantidad_instrumentos_inversion_min):
        nombre_menos_inversion=nombre
        cantidad_instrumentos_inversion_min=cantidad_instrumentos
print (f"el nombre del usuario que menos invirtio es {nombre_menos_inversion} y la cantidad de instrumentos es de: {cantidad_instrumentos_inversion_min}")

# d. Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000
if (monto>20000 and monto<50000):
    porcentaje_mep=contador_mep*100/contador_usuarios

print (f"porcentaje de usuarios que invirtieron en mep, con un monto entre 20000 y 50000 es: {porcentaje_mep}") 