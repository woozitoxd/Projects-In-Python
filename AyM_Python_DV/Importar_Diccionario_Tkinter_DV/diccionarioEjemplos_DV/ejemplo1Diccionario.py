precios = {
    "Manzana": 1.50,
    "Banana": 2.75,
    "Pera": 5.20
}
# Acceder al precio de la Banana
print(precios["Banana"])  # Salida: 2.75
#Asi es como usamos un diccionario en Python

#Podemos agregar, modificar y eliminar elementos
precios["Naranja"] = 3.00  # Agregar
precios["Pera"] = 4.80     # Modificar
del precios["Manzana"]     # Eliminar
print(precios)  # {'Banana': 2.75, 'Pera': 4.8, 'Naranja': 3.0}

#Cómo lo recorremos
for fruta, precio in precios.items():
    print(f"{fruta}: ${precio}")

#Comprbar si una clave existe
if "Banana" in precios:
    print("El precio de la Banana es:", precios["Banana"])  
else:
    print("La Banana no está en el diccionario.")
    


#Dentro de un diccionario podemos tener listas, tuplas, otros diccionarios, etc.
#Ejemplo:
datos = {
    "nombres": ["Ghami", "Elias", "Gabi"],
    "edades": (25, 30, 20),
    "direccion": {
        "calle": "Calle Falsa 123",
        "ciudad": "Da Vinci"
    }
}