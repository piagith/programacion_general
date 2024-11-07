

print ("Hola, a continnuacion le pediremos que ingrese algunos datos para determinar la posicion:" )
altura = float(input("Por favor, ingrese su altura en cm: "))

if altura < 160 or 1.60:
    print ("Su altura corresponde a la posicion de Base")
elif altura <= 160 or 1.60 and altura<=179 or 1.79:
    print ("Su altura corresponde a la posicion de escolta")
elif altura >=180 or 1.80 and altura<=199 or 1.99:
    print ("su altura corresponde a la posicion de alero")
elif altura >=200 or 2.00:
    print ("su altura corresponde a ala-pivot o pivot")

