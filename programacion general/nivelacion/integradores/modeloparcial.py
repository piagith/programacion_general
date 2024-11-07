validar="si"
flag_masculino_con_menos_edad=True
nombre_menos_edad="-1"
contador_nojubilados=0

contador_general=0
contador_femenino=0
contador_m=0
contador_o=0
menor_edad=0

contador_f_pintura=0
acum_edad_f_pintura=0
acum_votos_pintura_fem=0

validar=input("Desea ingresar votos?: (si/no) ")
while (validar=="si"):    
    nombre=input("ingrese su nombre: ")

    edad= int(input("ingrese su edad: "))
    while (edad<18):
        print("edad ingresada invalida")
        edad=int(input("vuelva a ingresar su edad: "))

    jubilado=input("Usted esta jubilado/a: 'si'  o 'no'")
    while (jubilado != "si" and jubilado != "no"):
        print("dato ingresado invalido ")
        jubilado=input("respuesta invalida, vuelva a ingresar la respuesta: ")

    genero= input("ingrese su genero (masculino-femenino-otro:  ")
    while (genero !="femenino" and genero !="masculino" and genero !="otro"):
        print("genero ingresado invalido: ")
        genero=input("ingrese su genero nuevamente: (femenino, masculino u otro: )")
    
    voto=input("ingrese su voto: (yoga, cine, pintura): ")
    while (voto!= "yoga" and voto!="cine" and voto !="pintura"):
        print ("voto ingresado invalido, vuelva a ingresar su voto (yoga, cine, pintura: )")
    contador_general+=1
    validar="desea seguir ingresando votos?: (si/no): "
    if (validar=="no"):
        print ("proceso finalizado")
        
    
    
    if (genero=="masculino"):
        contador_m+=1
    
    if (flag_masculino_con_menos_edad==True):
        flag_masculino_con_menos_edad=False

        menor_edad=edad

        nombre_menos_edad=nombre
        menor_voto=voto
    elif (edad < menor_edad):
        menor_edad=edad
        nombre_menos_edad=nombre
        menor_voto=voto
    elif (genero=="femenino"):
      contador_femenino+=1

    if (voto=="pintura"):
        contador_f_pintura+=1
        acum_votos_pintura_fem+=edad
else:
    contador_o+=1

if (jubilado=="no" and (voto=="cine" or voto =="pintura") and (edad > 24 and edad <51)):
    contador_nojubilados+=1

validar=input ("desea seguir? si/no  ")

    
print (f"cantidad de encuestados no jubilados que votaron por cine o pintura, dentro del rango de edad de 25 y 50 inclusive: {contador_nojubilados}")

if (nombre_menos_edad=="-1"):
    print ("no se ingresaron hombres")
else:
    print (f"nombre y voto del encuestado de genero masculino con menor edad: {nombre_menos_edad}|| {menor_edad}")

porcentaje_m= contador_m*100/contador_general
porcentaje_fem=contador_femenino*100/contador_general
porcentaje_o=contador_o*100/contador_general
print (f"procentaje masculino: {porcentaje_m}, porcentaje femenino :{porcentaje_fem},porcentaje de otro: {porcentaje_o}")

if (contador_f_pintura!=0):
    promedio=acum_edad_f_pintura/contador_f_pintura
    print (f"promedio de edad de los encuestados de genero femenino es de{promedio}")
else:
    print ("no se ingresaron mujeres")

mas_encuestado="otro"
if (contador_femenino>contador_m and contador_femenino>contador_o):
    mas_encuestado="femenino"
elif (contador_m>contador_o):
    mas_encuestado="masculino"
print (f"el genero con mas encuestdos fue: {mas_encuestado}")