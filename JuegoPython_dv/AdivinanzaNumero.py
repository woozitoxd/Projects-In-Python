#Juego de adivinanzas de un número usando librería random
#Agregar validaciones de letras


import random



try:
    num = random.randint(1, 100) #El numero se asigna  num de un intervalo entre 1 y 100
    numeroUser = int(input("Adivine el número! (Elegir entre 1 y 100): "))
    while True:

        if (num > numeroUser):
            numeroUser = int(input(f"Tu número es muy grande! Restale un poco más... {num}:"))
        elif (num < numeroUser):
            numeroUser = int(input(f"Tu número es muy chico! Sumale un poco más...{num} :"))
        elif (num == numeroUser):
            print(f"Felicitaciones, ganaste! el número era: {num}")
            break
except ValueError:
    print("Ingresaste un carácter no válido, intenta denuevo con un NÚMERO ENTERO")
    
