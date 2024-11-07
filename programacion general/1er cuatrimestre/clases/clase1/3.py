'''
dado un numero n, verifica si es multiplo de 3 
y al mismo
tiempo, si es mayor que 50.
muestra el resultado de ambas comparaciones
en una sola expresion.
'''

n = 60

resultado = (n > 50) and (n % 3 == 0)

print (resultado)
