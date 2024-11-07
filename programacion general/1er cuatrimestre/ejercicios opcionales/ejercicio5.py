# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 80 ARS y si es mayor de 18 años, 150 ARS.

contador=0
print ("BIENVENIDOS A FICHIN")

entrada=input("desea adquirir entradas/fichines: si or no: ")
while entrada =="si":
    edad=int(input("ingrese su edad: "))
    
    if edad<4:
         print ("el valor de la entrada para los menores de 4 años es gratuita")
    elif edad >=4 and edad <=18:
        print ("el valor de la entrada es de 80 ars")
    else: 
        print ("el valor de la entrada para los mayores de 18 años es de 150 ars")
        
    entrada=input("desea seguir comprando fichines/entradas: si o no: ")
    if entrada=="no":
        print("gracias por su compra, disfrute")   
    contador+=1
