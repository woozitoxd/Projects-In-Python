import random


#Con Not verificamos si está vacia, en realidad la negamos
cadena = ""

if not cadena:
    print("La cadena está vacía.")
else:
    print("La cadena no está vacía.")

#Otra forma de verificarlocadena = ""

if cadena == "":
    print("La cadena está vacía.")
else:
    print("La cadena no está vacía.")


#Invertir cadena

cadena = "hola"
cadena_invertida = cadena[::-1]
print(cadena_invertida)  # Salida: "aloh"

#Contar caracteres

cadena = ""

if len(cadena) == 0:
    print("La cadena está vacía.")
else:
    print("La cadena no está vacía.")
    




import random

print(random.randrange(10))  # Números entre 0 y 9

import random

print(random.randint(10, 20))  # Números entre 10 y 20


import random

print(random.choice(["PHP", "Java", "Python"]))



for i in range(5):
    print(i)  # Imprime del 0 al 4