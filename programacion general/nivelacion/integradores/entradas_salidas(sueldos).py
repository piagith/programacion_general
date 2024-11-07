#1

print("Bienvenidos a la UTN")
#2
nombre= input("Por favor, ingrese su nombre: ")
print ("Hola" ,nombre,)
#3
edad=int(input("A continuacion, ingrese su edad: "))
nombre =input ("Ahora, ingrese su nombre: ")

print (f"Usted se llama {nombre} y tiene {edad} años")

#4
operador_a= int(input("ingrese un numero: "))
operador_b=int (input("ingrese otro numero: "))

suma=operador_a + operador_b
print ("el resultado de la suma es: ",suma)

#5
operador_a= int(input("ingrese un numero: "))
operador_b=int(input("ingrese otro numero: "))
suma_2=operador_a+operador_b
resta_2=operador_a-operador_b
division_2=operador_a/operador_b
multiplicacion_2=operador_a*operador_b


print("el resultado de la suma es: ",suma_2)
print("el resultado de la resta es:", resta_2)
print ("el resultado de la division es :",division_2)
print ("el resultado de la multiplicacion es :", multiplicacion_2)
#6

operador_a =int(input("ingrese un numero: "))
operador_b=int (input("ingrese un numero: "))

resto=operador_a%operador_b
print (f"el resto de dividir {operador_a} por {operador_b} es: ", resto)


#7
sueldo= float(input("ingrese su sueldo: "))
incremento=0.15
sueldo_incremento= sueldo *0.15
sueldo_actualizado= sueldo + sueldo_incremento
print ("el sueldo actualizado con el incremento del 15% es de: ", sueldo_actualizado)

#8

sueldo=int(input("ingrese el sueldo: "))
incremento =float(input("ingrese el incremento: "))

print("su sueldo es de:", sueldo," y su incremento es de: ", incremento)

sueldo_incremento_porcentual= sueldo + incremento
print ("Entonces su sueldo actualizado con el incremento y sueldo ingresado es de: ", sueldo_incremento_porcentual)

#9
importe=int(input("por favor, ingrese el importe"))
descuento =(importe*20) / 100

importe_act=importe - descuento
print ("el importe actualizado con un descuento del 20% es de:", importe_act)

#10
importe=int(input("ingrese el importe deseado: "))
descuento=int(input("ingrese el descuento: "))

importe_actualizado= importe - descuento
print ("el importe actualizado con el descuento aplicado es de:" ,importe_actualizado)

