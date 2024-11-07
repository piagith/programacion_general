'''
variable=0

for i in range (1, 6):
    variable +=i


print ("la suma es", variable)
 
'''

#funciona de la misma manera con for o while
'''
sum = 0
i = 1
while i < 6:
    sum += i
    i += 1
  
print ("la suma es: ", sum)
'''
'''
suma_total = 0
numero = int (input("ingrese un numero o (o para terminar) :"))
while numero !=0:
    suma_total+=numero
    numero = int (input("ingrese otro numero o (0 para terminar) :"))

print (f"la suma total es de: {suma_total}")
'''

'''
acum = 0
numero = int(input("ingrese la cantidad de notas: "))


for i in range (numero):
    nota = int(input(f"ingrese la nota:{i + 1} "))
    acum += nota

promedio = acum / numero
print (f"el promedio del estudiantr es de : {acum / numero}")

'''
'''
cont = 0
acum = 0

numero = int (input("ingrese la cantidad de notas: "))

while cont < numero:
    nota = int(input(f"ingrese la nota:  {cont +1} "))
    acum += nota
    cont +=1

print (f"el promedio del estudiante es de {acum / numero}")


'''

'''
total_carrito = 0

precio = float (input("ingrese el precio del producto (o 0 oara terminar): "))

while precio !=0:
    total_carrito += precio
    precio = float (input("ingrese el precio del producto (o 0 oara terminar): "))


print (f"el total acumulado en el carrito es de {total_carrito} dolares")

'''