cont = 0
numero_maximo = float('-inf')
numero_minimo = float('inf')

while cont < 4:
    numero = float(input("Ingrese un número: "))

    if numero > numero_maximo:
        numero_maximo = numero
    
    if numero < numero_minimo:
        numero_minimo = numero
    
    cont += 1

print("\nBucles relizados:", cont)
print("Valor máximo:", numero_maximo)
print("Valor mínimo:", numero_minimo)