
#Creación de la lista
lista = [1, 2, 3, 4]

#Acceder a elementos
lista[0]  # Primer elemento
lista[-1] # Último elemento

#Cambiar elementos
lista[2] = 10  # Cambia el valor de la tercera posición

lista.append(6)        # Agrega al final
lista.insert(1, 8)     # Inserta en la posición 1
lista.remove(8)        # Elimina la primera aparición del 8
elemento = lista.pop() # Elimina y devuelve el último elemento

if 4 in lista:
    print("4 está en la lista")
    
for elemento in lista:
    print(elemento)


#Utilizar cada una para modificar listas 



#Listas COMPLEJAS

producto = ["Notebook", 899.99, 10, True]

#Lista de Listas

productos = [
    ["Notebook", 899.99, 10, True],
    ["Mouse", 19.99, 50, False]
]

#Recorrer listas

for producto in productos:
    nombre = producto[0]
    print(f"Producto: {nombre}")
    
#Obtener toda la info
productos = [
    ["Notebook", 899.99, 10, True],
    ["Mouse", 19.99, 50, False]
]


for producto in productos:
    nombre = producto[0]
    precio = producto[1]
    stock = producto[2]
    oferta = "Sí" if producto[3] else "No"
    
    print(f"Producto: {nombre}, Precio: {precio}, Stock: {stock}, En oferta: {oferta}")
