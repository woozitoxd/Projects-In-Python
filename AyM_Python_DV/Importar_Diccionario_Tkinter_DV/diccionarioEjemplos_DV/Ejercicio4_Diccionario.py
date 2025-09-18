inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "bananas": 20
}

print("Inventario inicial:", inventario)

# Consultar producto
producto = "naranjas"
if producto in inventario:
    print(f"Hay {inventario[producto]} {producto}")

# Actualizar cantidad
inventario["manzanas"] += 5
inventario["bananas"] -= 3

print("Inventario actualizado:", inventario)
