productos = [
    ["manzana", 200, 50],
    ["banana", 150, 30],
    ["pan", 500, 20]
]

def mostrar_productos(lista):
    for nombre, precio, stock in lista:
        print(f"{nombre} - ${precio} - Stock: {stock}")

def buscar_producto(lista, nombre):
    for producto in lista:
        if producto[0] == nombre:
            return producto
    return None

def valor_total(lista):
    total = 0
    for nombre, precio, stock in lista:
        total += precio * stock
    return total

num = 1
while num != 0:
    print("\nIngrese la opcion deseada: \n1. Mostrar Productos \n2. Buscar Producto \n3. Valor total del inventario\n0. Para Salir \n")
    num = int(input("Número: "))
    match num:
        case 0:
            print("Saliendo")
        case 1:
            mostrar_productos(productos)
        case 2:
            print(buscar_producto(productos, "banana"))
        case 3:
            print("Valor total del inventario:", valor_total(productos))
        case default:
            print("Opción inválida. Por favor, intente nuevamente.")