import random

# Pedir el nombre y verificar que no esté vacío
nombre = input("Ingrese su nombre: ").strip()
while not nombre:
    print("El nombre no puede estar vacío.")
    nombre = input("Ingrese su nombre: ").strip()

# Mostrar el nombre invertido y su longitud
print(f"Nombre invertido: {nombre[::-1]}")
print(f"Longitud del nombre: {len(nombre)}")

# Generar número aleatorio entre 1 y 10
numero_secreto = random.randrange(1, 10)
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    entrada = input(f"Intento {intentos+1}/{max_intentos}. Adivina el número (1-10): ")
    if not entrada.isdigit():
        print("Tenes ingresar un número entero.")
        continue

    intento = int(entrada)

    if intento == numero_secreto:
        print("¡Ganaste!")
        break
    else:
        print("Incorrecto. Intentos restantes: ", max_intentos - intentos - 1)
    
    intentos += 1
else:
    print(f"Se acabaron los intentos. El número era {numero_secreto}. Gracias por jugar.")