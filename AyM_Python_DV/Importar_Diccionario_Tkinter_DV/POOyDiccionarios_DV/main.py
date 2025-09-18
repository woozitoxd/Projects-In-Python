from alumno import Alumno

# Diccionario de alumnos, clave = DNI, valor = objeto Alumno
alumnos = {}

def agregar_alumno():
    nombre = input("Ingrese nombre del alumno: ")
    dni = input("Ingrese DNI: ")
    if dni in alumnos:
        print("El alumno ya existe.")
    else:
        alumnos[dni] = Alumno(nombre, dni)
        print("Alumno agregado correctamente.")

def agregar_nota():
    dni = input("Ingrese DNI del alumno: ")
    if dni in alumnos:
        materia = input("Ingrese materia: ")
        nota = int(input("Ingrese nota: "))
        alumnos[dni].agregar_nota(materia, nota)
        print("Nota agregada.")
    else:
        print("Alumno no encontrado.")

def mostrar_todos():
    if not alumnos:
        print("No hay alumnos cargados.")
    for alumno in alumnos.values():
        alumno.mostrar_info()

# --- Menú principal ---
while True:
    print("\n--- Sistema de Gestión de Alumnos ---")
    print("1. Agregar alumno")
    print("2. Agregar nota")
    print("3. Mostrar todos los alumnos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        agregar_nota()
    elif opcion == "3":
        mostrar_todos()
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")
