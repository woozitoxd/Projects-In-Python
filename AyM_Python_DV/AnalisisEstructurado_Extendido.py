import sqlite3

conn = sqlite3.connect("hotelExtendido.db")
cursor = conn.cursor()

# Crear tablas si no existen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        tipo TEXT NOT NULL
    )
''')

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

# Insertar algunos usuarios (si no existen)
usuarios_iniciales = [
    ("Luis", "cliente"),
    ("Sofia", "admin")
]

cursor.executemany('''
    INSERT INTO usuario (nombre, tipo)
    SELECT ?, ? WHERE NOT EXISTS (
        SELECT 1 FROM usuario WHERE nombre = ? AND tipo = ?
    )
''', [(u[0], u[1], u[0], u[1]) for u in usuarios_iniciales])
conn.commit()

# --- FUNCIONES ---

def login():
    nombre = input("Ingrese su nombre: ")
    cursor.execute("SELECT * FROM usuario WHERE nombre = ?", (nombre,))
    user = cursor.fetchone()
    if user:
        print(f"Bienvenido, {user[1]} ({user[2]})")
        return user
    else:
        print("Usuario no encontrado.")
        return None


def hacer_reserva(nombre_cliente):
    entrada = input("Fecha de entrada (YYYY-MM-DD): ")
    salida = input("Fecha de salida (YYYY-MM-DD): ")
    habitacion = int(input("Número de habitación: "))
    cursor.execute('''
        INSERT INTO reserva (nombre_cliente, fecha_entrada, fecha_salida, habitacion)
        VALUES (?, ?, ?, ?)
    ''', (nombre_cliente, entrada, salida, habitacion))
    conn.commit()
    print("Reserva confirmada.")



def ver_reservas():
    cursor.execute("SELECT * FROM reserva")
    reservas = cursor.fetchall()
    for r in reservas:
        print(f"ID: {r[0]}, Cliente: {r[1]}, Entrada: {r[2]}, Salida: {r[3]}, Habitación: {r[4]}, Estado: {r[5]}")

def cancelar_reserva():
    id_reserva = int(input("Ingrese el ID de la reserva a cancelar: "))
    cursor.execute("UPDATE reserva SET estado = 'cancelada' WHERE id = ?", (id_reserva,))
    conn.commit()
    print("Reserva cancelada.")


# --- SIMULADOR DE SISTEMA ---
def iniciar_sistema():
    user = login()
    if not user:
        return
    if user[2] == "cliente":
        hacer_reserva(user[1])
    elif user[2] == "admin":
        while True:
            print("\n1. Ver reservas\n2. Cancelar reserva\n3. Salir")
            opc = input("Opción: ")
            if opc == "1":
                ver_reservas()
            elif opc == "2":
                cancelar_reserva()
            elif opc == "3":
                break
            else:
                print("Opción inválida.")

# Ejecutar
iniciar_sistema()

conn.close()
