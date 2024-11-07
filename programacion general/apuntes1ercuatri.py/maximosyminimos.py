#bucle for, una vez que termine el bucle, mostrar el maximo ingresado
'''
#para numeros positivos
numero_max = 0

for i in range (1, 6):
    numero = int(input(f"ingrese el numero: {i} "))
    if numero > numero_max:
        numero_max = numero
    
print ("el numero maximo es: ", numero_max)
'''
#para numeros negativos

numero_max = float("-inf")

for i in range (1, 6):
    numero = int(input(f"ingrese el numero: {i} "))
    if numero > numero_max:
        numero_max = numero
    
print ("el numero maximo es: ", numero_max)


#numero minimo

numero_min = float("inf")

for i in range (1, 6):
    numero = int(input(f"ingrese el numero: {i} "))
    if numero < numero_max: #se cambia el signo
        numero_min = numero
    
print ("el numero maximo es: ", numero_min)