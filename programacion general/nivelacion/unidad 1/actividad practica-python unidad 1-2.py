edad = int (input ("por favor,ingrese su edad: "))
if edad==18:
    print ("usted tiene 18 años")

if edad >=18 :
    print ("usted es mayor de edad")
else: 
    print ("usted es menor de edad")


print("Ahora verificaremos su altura")
altura = float(input("por favor, ingrese su altura en metros: "))
if altura > (180 or 1.80):
        print("usted puede ser pivot")
else:
        print ("usted no es pivot")


print("Ahora veremos y le asignaremos una categoria segun su edad")

edad=int(input("por favor, vuelva a ingresar su edad: "))
if edad<=10:
      print("usted pertenece a la categoria de niños y niñas")
elif edad>=10 and edad<13:
      print("usted pertenece a la categoria de pre-adolescente")      
elif edad>10 and edad<=17:
      print("Es adolescente!! Por lo tanto usted pertenece a la categoria de adolescentes")
else: 
      print("usted pertenece a la categoria de mayores/adultos")
