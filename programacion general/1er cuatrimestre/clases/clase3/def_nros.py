def sumar(num1, num2):
    resultado = num1 + num2
    print(resultado)


num1 = int(input("ingrese numero 1: "))
num2 = int(input("ingrese numero 2: "))

sumar(num1, num2)

######################

def restar(num1, num2):
    resultado = num1 - num2
    print(resultado)

    number1 = int(input("ingrese numero 1: "))
    number2 = int(input("ingrese el numero 2: "))


    restar(num2=number2, num1=number1)

########################

def saludar(nombre):
    saludo = f"hola {nombre}"
    return saludo


saludar("fabio")
print (saludar)

###########################
#len devuelve cantidad de caracteres que tiene un string
variable = "rodrigo"

print(len(variable))

#########################

def contar_caracteres(texto):
    contador = 0
    for i in texto:
        contador += 1
    return contador



texto = "hola"
contar_caracteres(texto)


#############################
texto = "hola"
for i in texto:
    print(i)