
sueldo=int(input("ingrese el sueldo $"))
incremento_porcentaje= int(input("ingrese el incremento: "))

sueldo_incrementado= (sueldo*incremento_porcentaje)/100

sueldo_total=sueldo+sueldo_incrementado
print("su sueldo es de", sueldo, "pesos. El incremento porcentual ingresado es de",incremento_porcentaje,"%, por ende su sueldo actualizado con el incremento es de", sueldo_total, )
