word=input("ingrese una palabra: ")
for i in range(10):
    print (word)

edad=int(input("ingrese su edad: "))
for i in range (edad):
    print("has cumplido" + str (i+1)+ "años")

numeroentero=int(input("ingrese un numero entero: "))
for i in range (1, numeroentero+1, 2):
    print (i, end=", ")

numeroentero=int(input("ingrese un numero positivo: "))
for i in range (numeroentero, -1, -1):
    print (i, end=", ")


acumulador=float(input("cantidad a invertir: "))
interes=float(input("interes porcentual anual: "))
años=int(input("años: "))
for i in range (años):
    acumulador*=1+interes/100
    print ("capital tras "+str(i+1) + "años: " + str (round(acumulador, 2)))


        