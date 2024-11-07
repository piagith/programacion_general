#funicon iterativa
'''
def contar_hasta_Cero (numero):
    for i in range (10, -1, -1):
        print (i)

contar_hasta_Cero(10)


#funcion recursiva

def contar_recursivamente (numero):
    if numero < 0:
        return
    print(numero)
    contar_recursivamente(numero - 1)

contar_recursivamente(10)

def factorial_iterativo (numero):
    if numero < 0:
        return "el factorial no se puede realizar"
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range ( 0, numero):
            resultado *= i
        return resultado
    
print (factorial_iterativo(0))'''



def factorial_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial_recursivo (numero - 1)
    
factorial_recursivo (5)