x = True
print(not x)  # Salida: False

y = False
print(not y)  # Salida: True

# Ejemplo con una condición
a = 5
b = 10
if not a > b:
    print("a no es mayor que b")  # Se ejecuta porque a > b es False
else:
    print("a es mayor que b")