nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

print(f"Hola {nombre}! ¿Cómo estás?")



print(f"Edad es de tipo: {type(edad)}")
print(f"Ahora edad es de tipo: {type(int(edad))}")

if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("No sos mayor de edad.")