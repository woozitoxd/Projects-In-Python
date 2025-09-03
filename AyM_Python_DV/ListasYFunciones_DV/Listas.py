#En lugar de hacer esto:
cuadrados = []
for x in range(1, 6):
    cuadrados.append(x**2)

#Podemos usar una lista de comprensión:

#Esto es una Lista de comprensión, se crea la lista "cuadrados" con los cuadrados de los números del 1 al 6.
cuadrados = [x**2 for x in range(1, 7)]
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]



#Acá una lista con los números pares de otra lista creada previamente.
numeros = [3, 7, 10, 15, 20]
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # [10, 20]


numeros = []
for num in range(1, 11):
    if num % 2 == 0:
        numeros.append(num)
print(numeros)  # [2, 4, 6, 8, 10]


lista = [1, 2, 3, 4, 5, 10, 7, 90]

lista.sort()  # Ordena la lista en su lugar
print(lista)  # Salida: [1, 2, 3, 4, 5, 7, 10, 90]

lista.sort(reverse=True)  # Ordena la lista en orden descendente
print(lista)  # Salida: [90, 10, 7, 5, 4, 3, 2, 1]


#Ordenar una lista de cadenas por su longitud
palabras = ["manzana", "kiwi", "banana", "cereza"]
palabras.sort(key=len)
print(palabras)  # Salida: ['kiwi', 'banana', 'cereza', 'manzana']

for palabra in palabras:
    print(palabra)