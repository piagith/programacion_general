numero=1
numeros_pares=1
while numero>10:
    if numero %2==0:
        numeros_pares +=1
print("la suma de los numeros pares es:", numeros_pares)


contraseña=input  ("ingrese la contraseña: ")
while contraseña != "utn750":
    contraseña= input ("contraseña incorrecta, intente nuevamente: ")
print ("ha accedido con exito, contraseña correcta")


numero=int(input("ingrese un numero: "))
while numero >9 or numero <0:
    numero =int(input("intente nuevamente: "))
print ("el valor que usted ingreso es:",numero, "genial!")


letra=input("ingrese una letra: ")
letra1 ="_"
letra2 ="_"
letra3 ="_"
palabra=""

while palabra !="UTN":
    letra=input ("ingrese otra letra: ")
    if letra =="U":
        letra1=letra
        palabra=letra1+letra2+letra3
        print(palabra)

    if letra=="T":
        letra2=letra
        palabra=letra1+letra2+letra3
        print(palabra)

    if letra =="N":
        letra3=letra
        palabra=letra1+letra2+letra3
        print(palabra)




contador=0
acumulador=0
promedio=0.0
numeros=5 

while contador < numeros:
    numero= int(input("ingrese un numero: "))
    acumulador +=numero
    contador +=1
    promedio =acumulador / numeros
print ("valor total: ", acumulador, "\npromedio:", promedio)