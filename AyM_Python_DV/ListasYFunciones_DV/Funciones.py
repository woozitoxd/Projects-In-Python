def saludar():
    print("Hola, ¿Todo bien?")
    
#Acá también importa la identación.


def saludar(nombre):
    print(f"Hola {nombre}, ¿Todo bien?")

saludar("Elias")    

def saludar(nombre="Sin Nombre"):
    print(f"Hola {nombre}, ¿Todo bien?")
    
saludar()

def sumar(*numeros):
    return sum(numeros)

print(sumar(1,2,3,4,5))