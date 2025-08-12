def main():
    print("Hola, este es el programa principal.")

if __name__ == "__main__":
    main()
    


#diccionarios:
precios = {
    "Manzana": 1.50,
    "Banana": 0.75,
    "Naranja": 1.00
}
# Acceder a un valor:
print(precios["Manzana"])  # Salida: 1.50

# Agregar o modificar
precios["Pera"] = 1.20

# Eliminar
del precios["Banana"]

# Recorrer diccionario
for fruta, precio in precios.items():
    print(f"{fruta}: ${precio}")