# Lista de productos
productos = []

# Función para agregar productos
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    productos.append([nombre, precio, stock])
    print(f"Producto '{nombre}' agregado con éxito.")

# Función para mostrar todos los productos
def mostrar_productos():
    if not productos:
        print("No hay productos en la lista.")
    else:
        for i, producto in enumerate(productos, start=1):
            nombre, precio, stock = producto
            print(f"{i}. {nombre} - Precio: ${precio:.2f} - Stock: {stock}")

# Función para buscar un producto por nombre
def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    for producto in productos:
        if producto[0].lower() == nombre.lower():
            print(f"Producto '{nombre}' encontrado:")
            print(f"Precio: ${producto[1]:.2f} - Stock: {producto[2]}")
            return
    print(f"Producto '{nombre}' no encontrado.")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = sum(precio * stock for _, precio, stock in productos)
    print(f"Valor total del inventario: ${total:.2f}")

# Función para eliminar un producto
def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productos:
        if producto[0].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado con éxito.")
            return
    print(f"Producto '{nombre}' no encontrado.")

# Menú principal
while True:
    print("\nMenú de opciones:")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Calcular valor total")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Ingrese la opción deseada: ")

    match opcion:
        case "1":
            agregar_producto()
        case "2":
            mostrar_productos()
        case "3":
            buscar_producto()
        case "4":
            calcular_valor_total()
        case "5":
            eliminar_producto()
        case "6":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida. Por favor, intente nuevamente.")