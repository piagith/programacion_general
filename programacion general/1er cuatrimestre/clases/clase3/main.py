#ejemplo ejercicio en clase


#sintaxis

#palabra reservada : "def"
#nombre de la funcion, lo que va dsp del def+parentesis


def saludar():
    saludo = "estoy saludando desde la funcion"
    print(saludo)

#llamar a la funcion

saludar()

#si queres ponerlo o llamarla otra vez se vuelve a llamar la funcion:
#saludar()


def saludar(nombre):
    saludo = f"hola, como estas {nombre}?"

    print(saludo)

name = input("ingresa tu nombre: ")
saludar(name)


def saludar(nombre):
    saludo = f"hola, como estas {nombre}?"
    print (saludo)

nombre = input("ingresa tu nombre: ")
saludar (nombre)