print("Bienvenido al Cine")

# Pedimos datos
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tenés? "))
hora_actual = int(input("¿Qué hora es? (0-23) "))


puede_A = edad >= 18 and edad <= 30 and 18 <= hora_actual <= 22
puede_B = (edad < 18 or edad > 60) and 16 <= hora_actual <= 20
puede_C = not (hora_actual >= 18)  # antes de las 18 hs

# Decisión del cine
if puede_A:
    print(f"{nombre}, ¡podés ver la Película 'Titanes del Pacífico'!") # Película A: 18-30 años, 18 a 22 hs

elif puede_B:
    print(f"{nombre}, ¡podés ver la Película 'John Wick'!") # Película B: menores de 18 o mayores de 60, 16 a 20 hs

elif puede_C:
    print(f"{nombre}, ¡podés ver la Película 'Como entrenar a tu dragón") # Película C: todos pueden ver, solo antes de las 18 hs

else:
    print(f"{nombre}, lo sentimos, no hay funciones disponibles para tu edad o hora")