# Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos 
# ingresos iguales o superiores a 20000 ARS mensuales. Escribir un programa que pregunte 
# al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que pagar un impuesto o no.

edad = int(input("por favor ingrese su edad: "))
ingresos = float (input("por favor ingrea tus ingresos mensuales en ars: "))

if edad > 0 :
    if edad >=18 and ingresos >=20000:
        print ("debes pagar el impuesto")
    else:
        print ("no estas obligado a pagar impuestos ")
else:
    print("ingrese una edad correcta")

