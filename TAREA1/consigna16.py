def saludar(): 
    print("Hola, ¿cómo estás?")
    
saludar()
#Vease que así como con las demás estructuras tipo for, if etc tenemos que tabular.

#Ingresando parámetros:
    
def saludar(nombre="sin nombre"): 
    print(f"Hola, {nombre}, ¿cómo estás?")

saludar()

#Multiples parámetros:
def sumar_todo(*numeros):
    return sum(numeros)

print(sumar_todo(1, 2, 3, 4))  # Devuelve 10



def sin_return():
    print("Esto no devuelve nada")

resultado = sin_return()
print(resultado)  # Imprime: None

sin_return()

def con_return():
    return("Esto devuelve un mensaje")

resultado = con_return()
print(resultado)  #Devuelve el mensaje específicado en el return en lugar de imprimir "None"