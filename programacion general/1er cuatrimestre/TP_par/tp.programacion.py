
continuar = "s"
 
inventario = [
    ["Chupetin Sable de Luz", 50, 200],
    ["Agua La Fuerza", 35, 3200],
    ["Gomitas Holocubo", 25, 990],
    ["Barrita de Cereal Wookiee", 48, 2500],
    ["Galletitas R2D2", 20, 15500],
]
continuar = input("Bienvenidos/as al quiosco yoda snack´s, desea continuar: s/n ")

    
def mostrar_menu(menu: int) -> str:
    menu = print('''
        Menu:
          1. Agregar producto al inventario
          2. Realizar una venta
          3. Mostrar productos disponibles
          4. Salir del sistema
          elija una opcion: 
          
''')
    opcion = input("Elija una opcion: ")
    match opcion:
        case "1":
            print("Agregar producto al inventario")
            agregar_producto(inventario)
        case "2":
            print("Realizar una venta")
            realizar_venta(inventario)
        case "3":
            print("Mostrar productos disponibles")
            mostrar_productos(inventario)
        case "4":
            print("Salir del sistema")
            salir ()
        case _:
            print("Incorrecto, eliga una opcion valida")

    return(menu)

def agregar_producto (inventario: list) -> list: 
    nombre_producto = input("Ingrese nombre de producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio en pesos: "))

    for producto in inventario:
        if producto[0] == nombre_producto:
            producto[1] += cantidad
            producto[2] = precio
            print(f"Producto actualizado: {producto[0]}, nueva cantidad: {producto[1]}, nuevo precio: ${producto[2]:.2f}")
            return inventario
    inventario.append([nombre_producto, cantidad, precio])
    print(f"Producto agregado: {nombre_producto}, cantidad: {cantidad}, precio: ${precio:.2f}")
    continuar=input("desea ingresar mas productos: s/n ")

def realizar_venta (inventario: list) -> float:
    print(inventario)
    
    continuar = "s"
    
    while continuar == "s":
        producto_seleccionado = input("Seleccione el producto que desea comprar: ").lower()
        cantidad = int(input("Ingrese la cantidad: "))
        indice_encontrado = -1
        
        for i in range(len(inventario)):
            if inventario[i][0].lower() == producto_seleccionado.lower():  # Ignoramos mayúsculas/minúsculas
                indice_encontrado = i

        if indice_encontrado == -1:
            print("Producto no encontrado en el inventario.")
            return False

        if inventario[indice_encontrado][1] < cantidad:
            print(f"No hay suficiente cantidad de '{producto_seleccionado}'. Disponibles: {inventario[indice_encontrado][1]}.")
            return False
        
        precio_total = cantidad * inventario[indice_encontrado][2]
        inventario[indice_encontrado][1] -= cantidad  
        print(f"Venta realizada: {cantidad} de '{producto_seleccionado}' por un total de ${precio_total}.")
    
        continuar = input("¿Desea continuar agregando productos? s/n: ")
    return precio_total

def mostrar_productos(inventario : list)-> list:
    vacio = True
    for producto in inventario:
        if producto[1] > 0:
            nombre = producto [0]
            cantidad = producto[1]
            precio = producto[2]
            vacio = False
            print (f"producto: {nombre}, cantidad disponible: {cantidad}, precio:{precio} ")
    if vacio :
        print ("el inventario actualmente esta vacio.")
    continuar = input("desea continuar s/n: ")

def salir():
    print("saliendo de quiosco, hasta pronto.")

# mostrar_menu(continuar)
# agregar_producto(inventario)
# print(inventario)
# realizar_venta(inventario)
# mostrar_productos(inventario)

while continuar.lower() == "s":
    mostrar_menu(mostrar_menu)
    opcion = input('''
         Menu:
          1. Agregar producto al inventario
          2. Realizar una venta
          3. Mostrar productos disponibles
          4. Salir del sistema 
            seleccione una de las opciones: ''')
    
    match opcion:
        case "1":
            agregar_producto(inventario)
        case "2":
            realizar_venta(inventario)
        case "3":
            mostrar_productos(inventario)
        case "4":
            salir()
            break
        case _:
            print("opcion incorrecta, elija una opcion valida")

