#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato en la consola y muestre por pantalla el número de teléfono sin el prefijo y la extensión
#


print("Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56)")

numero = input("Ingrese su número de Telefono: ")

print("Numero: ", numero[4:-3]) #Acá estamos usando SLIDE, estamos diciendole que a la cadena que almaceno el numero, comienze a contar a partir del 4 caracter y le reste los ultimos 3
# numero[4:-3] = a partir del cuarto caracter y quitar los ultimos 3 caracteres