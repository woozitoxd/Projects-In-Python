



print("Hola mundo")

var = "hola"
#En caso de querer concatenar tenemos dos formas de hacerlo: 
print("Hola mundo " + var )
#El problema de esto es que solo podremos utilizar variables 
print("Hola mundo " , var )

nombre = "Candela"
edad = 24
print(f"Hola, {nombre}! tu edad es {edad}")  # Resultado: Hola, Elias! tu edad es 24

print(f"El año que viene tendré {edad + 1} años")  # Resultado: El año que viene tendré 31 años

type(edad)
print(type(edad))


#Convertir cadena a entero
y = "25"
y_int = int(y)  # Convierte cadena a entero
print(type(y_int))  # Salida: <class 'int'>

#Cadena a decimal
z = "3.14159"
z_float = float(z)  # Convierte cadena a float
print(type(z_float))  # Salida: <class 'float'>

z = 10
z_string = str(z)
print(type(z_string))




temperatura = 30 

if temperatura > 30:
    print("Hace calor") 
elif temperatura > 20: 
    print("Hace buen tiempo") 
else: 
    print("Hace frío")

# Nótese que se usa “:” para “abrir” y se usa la identación para diferenciar

x = 10
x += 5      # x ahora es 15
x *= 2      # x ahora es 30
x -= 10     # x ahora es 20
x /= 2      # x ahora es 10.0 (resultado float)

edad = 18

print(edad == 18)   # True
print(edad != 21)   # True
print(edad > 16)    # True
print(edad < 18)    # False
print(edad >= 18)   # True
print(edad <= 17)   # False


