# Cree un programa que calcule el IMC (Indice de masa corporal). Formula --> IMC=Peso/Altura2 (Peso sobre altura al cuadrado)
# El usuario debera ingresar su peso y su altura (su nombre si quieren y despues imprimirlo concatenado) y el programa ademas de 
# calcular el IMC debera decir en que clasificacion se encuentra.
# La clasificacion la encontraran el archivo de imagen: IMC_clasificacion.jpg

nombre= input("ingrese su nombre: ")
peso= float(input("ingrese su peso: "))
altura=float(input("ingrese su altura en cm: "))

imc= peso/(altura**2)
if imc<18.5:
    print ("indice masa corporal: bajo peso")
elif imc >=18.5 and imc <=24.9:
    print ("indice masa corporal: adecuado")
elif imc >=25.0 and imc <=29.9:
    print ("indice masa corporal: sobrepeso")
elif imc >=30.0 and imc<= 34.9:
    print ("indice masa corporal: obesidad grado 1")
elif imc >=35.0 and imc <=39.9:
    print("indice masa corporal: obesidad grado 2")
else: 
    print ("indice masa corporal: obesidad grado 2")
    