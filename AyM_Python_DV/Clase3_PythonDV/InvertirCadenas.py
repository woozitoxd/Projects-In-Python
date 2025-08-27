palabra = " Da Vinci "
print(palabra[::-1]) # Resultado devuelto: "icniV aD "


palabra = "Escuela Da Vinci"

print(len(palabra))  #Resultado devuelto: 16 (La cantidad de carácteres que contiene esa cadena)



#Validando palíndromos
palabra = "Neuquen"
if palabra == palabra[::-1]: #Comparamos la palabra ingresada con la palabra invertida
    print("Es un palíndromo")  
    

#Una forma de darle seguridad a las contraseñas (no recomendable)
clave = "micontrasenia123"
print("Contrasenia invertida:", clave[::-1])  