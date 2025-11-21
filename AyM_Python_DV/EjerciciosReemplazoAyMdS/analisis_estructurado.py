import sqlite3
from datetime import datetime

# 1. Conexión a la base de datos
conn = sqlite3.connect("hotelPrueba1.db")
cursor = conn.cursor()

# 2. Crear tabla de reservas (si no existe)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reserva (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_cliente TEXT NOT NULL,
        fecha_entrada TEXT NOT NULL,
        fecha_salida TEXT NOT NULL,
        habitacion INTEGER NOT NULL,
        estado TEXT DEFAULT 'confirmada'
    )
''')
conn.commit()


def Crear_Reserva(nombreCliente, fechaEntrada, fechaSalida, Reservahabitacion):
    cursor.execute('''
        INSERT INTO reserva (nombre_cliente, fecha_entrada, fecha_salida, habitacion) VALUES (?, ?, ?, ?)''', (nombreCliente, fechaEntrada, fechaSalida, Reservahabitacion))
    conn.commit()
    print("Reserva realizada :D")



def Formulario():
    print("Bienvenido al Formulario")
    nombre = input("Nombre del Cliente: ")
    fechaDeEntrada = input("Ingrese su fecha de entrada: ")
    fechaDeSalida = input("Ingrese su fecha de salida: ")
    habitacion = int(input("Ingrese su numero de habitacion: "))
    
    Crear_Reserva(nombre, fechaDeEntrada, fechaDeSalida, habitacion)
    

Formulario()


def verReservasAdmin():
    cursor.execute("SELECT * FROM reserva")
    reservas = cursor.fetchall()
    print("Reservas realizadas por los clientes:")
    for reservaLista in reservas:
        print(f"ID: {reservaLista[0]}, Cliente: {reservaLista[1]}, Fecha de Entrada: {reservaLista[2]}, Fecha de Salida: {reservaLista[3]}, Numero de Habitacion: {reservaLista[4]}")
    conn.close()


verReservasAdmin()

