for i in range(1, 6):
    print("Vuelta", i) 
    
    
    
#Bucle while

contador = 0
while contador < 5:
    print("Numero:", contador)
    contador += 1
    
    
#Break y Else con For

for i in range(5): #Prueben este código y cambien el 5 por un 3
    if i == 3:
        break
else:
    print("El bucle termino sin break")
    
    
#Break y else con while
numero = 0
while numero < 10:
    print("Soy menos que 10")
    numero = input("Ingrese numero:")
    if not numero.isdigit():
        print("La entrada esperada no es un número entero")
        break
    numero = int(numero)
else:
    print("Salgo del bucle normalmente porque se ingresó un número mayor o igual a 10")
    

#Usar Continue en Bucle While
numero = 0

while numero < 10:
    print("Soy menor que 10")
    entrada = input("Ingrese un número: ")

    if not entrada.isdigit():
        print("La entrada no es un número entero. Intentá de nuevo.")
        continue  # vuelve al inicio del bucle sin ejecutar lo de abajo
    numero = int(entrada)
else:
    print("Salgo del bucle porque se ingresó un número mayor o igual a 10")


#Simulando un do-while
while True:
    numero = int(input("Ingresar un número mayor a 0: "))
    if numero > 0:
        print(f"El numero ingresado es: {numero}" )
        break