#Juego del Ahorcado! Usando Listas.

import random

palabras = ["Python", "DaVinci", "Elias"]
palabra = random.choice(palabras).lower() #lower para que haga todo minuscula y no haya problemas con las mayusculas

adivinanza = ["_" for _ in palabra] #Lista que contiene un guion bajo por cada caracter en la palabra que eleigio el programa
intentos = 6

try:
    
    while intentos > 0 and "_" in adivinanza: #Mientras tengamos intentos y haya letras por adivinar, se ejecuta el bucle
        
        print(f"Palabra: "," ".join(adivinanza))
        letra = input(f"Adivina una letra: {palabra} ").lower()
        
        if letra in palabra:

            for i in range(len(palabra)): #La lista de adivanza se reemplaza en función de la letra en la palabra
                if palabra[i] == letra:
                    adivinanza[i] = letra
        else:
            intentos = intentos - 1
            print(f"¡Error! Te quedan {intentos} intentos. ")
        
            
    if "_" not in adivinanza:
        print(f"Ganaste! La palabra correcta fue: {palabra}")
    elif intentos == 0:
        print(f"Terminamos el juego, te quedaste sin intentos. la palabra era: '{palabra}'")
except ValueError:
    print("Se necesitaba un carácter válido.")
    