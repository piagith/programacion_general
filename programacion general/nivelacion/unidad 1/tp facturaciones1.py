producto1=float (input("ingrese el precio del primer producto: "))
producto2=float(input("ingrese el precio del segundo producto: "))
producto3=float(input("ingrese el precio del tercer producto: "))

suma=producto1+producto2+producto3
promedio=suma/3

print ("la suma de los tres productos es: ",suma)
print ("el promedio es: ",promedio)

iva=21
incremento=(suma*iva)/100
total =incremento + suma
print ("la suma de los tres productos mas el iva es:",total)
