#Contar carácteres de una cadena

texto = "Hola mundo"
print("Cantidad de caracteres:", len(texto))  #Resultado devuelto: 10



#Validar longitud de contraseña

password = input("Ingresá tu contraseña: ")
if len(password) < 8:
    print("La contraseña es demasiado corta")
else:
    print("Contraseña aceptada")
    
    
#Ejemplo 1: Contar carácteres de un nombre ingresado 
nombre = input("Ingresá tu nombre: ")
print("Tu nombre tiene", len(nombre), "letras")

#Ejemplo 2: Límitar cantidad de carácteres de un tweet
tweet = input("Escribí tu tweet: ")
if len(tweet) > 280:
    print("Tu tweet es demasiado largo")
else:
    print("Tweet publicado")