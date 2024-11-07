'''
pide al usuario que ingrese el valor de
 la base y la altura de un triangulo (float)
 calcula el area del triangulo utilizando la formula
 area = (base * altura)/2
 y muestra el resultado
'''


base = float(input("ingrese la base:"))
altura = float(input("ingrese la altura: "))

resultado = (base * altura) / 2

print (f"el area del triangulo es: {resultado}")
