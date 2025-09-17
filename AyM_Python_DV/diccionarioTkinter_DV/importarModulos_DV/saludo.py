def hola():
    print("¡Hola desde el módulo saludos!")

def adios():
    print("Chau desde el módulo saludos.")

if __name__ == "__main__":
    # Este bloque SOLO se ejecuta si corro directamente este archivo
    print("Ejecutando saludos.py directamente")
    hola()
    adios()
    
# Si importo este módulo en otro archivo, NO se ejecuta el bloque if __name__ == "__main__"
# pero puedo usar las funciones hola() y adios() desde ese otro archivo.