'''
cadena = """Loren ipsum i simply dummy text of
 the printing and typesetting industry"""

contador = 0
for caracter in cadena:
    if caracter == 's':
        contador += 1

print("la letra 's' aparece", contador, "veces en la cadena")
'''
#############################
#cambia/modifica el valor que queremos
lista = [45, 32, 19, 54]
print(lista)
print(id(lista))

lista[2] = 22

print (lista)
print(id(lista))
#####################################
#cadenas son inmutables: 
cadena = "astamos dormidos"
cadena [0] = "E"

print(cadena)
print(id(cadena))


cadena = "estamos dormidos"
print(cadena)
print(id(cadena))


############
cadena = "pithon"

cadena_2 = cadena[:1] + "y" + cadena[2:]

print(cadena_2)