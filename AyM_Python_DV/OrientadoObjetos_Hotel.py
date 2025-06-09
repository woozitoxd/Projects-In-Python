import sqlite3

# -------- MODELOS --------

class Usuario:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

class Cliente(Usuario):
    def hacer_reserva(self, sistema):
        print(f"Haciendo reserva para {self.nombre}")
        entrada = input("Fecha de entrada (YYYY-MM-DD): ")
        salida = input("Fecha de salida (YYYY-MM-DD): ")
        habitacion = int(input("Número de habitación: "))
        reserva = Reserva(self.nombre, entrada, salida, habitacion)
        sistema.guardar_reserva(reserva)
        print("Reserva realizada con éxito.")

class Admin(Usuario):
    def ver_reservas(self, sistema):
        print("Reservas actuales:")
        sistema.listar_reservas()

    def cancelar_reserva(self, sistema):
        id_reserva = input("Ingrese ID de la reserva a cancelar: ")
        sistema.cancelar_reserva(id_reserva)
        print("Reserva cancelada.")

class Reserva:
    def __init__(self, cliente, entrada, salida, habitacion):
        self.cliente = cliente
        self.entrada = entrada
        self.salida = salida
        self.habitacion = habitacion

# -------- SISTEMA PRINCIPAL --------

class SistemaReservas:
    def __init__(self):
        self.conn = sqlite3.connect("hotel_poo.db")
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                tipo TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reserva (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_cliente TEXT,
                fecha_entrada TEXT,
                fecha_salida TEXT,
                habitacion INTEGER,
                estado TEXT DEFAULT 'confirmada'
            )
        ''')
        self.conn.commit()

    def login(self):
        nombre = input("Ingrese su nombre: ")
        self.cursor.execute("SELECT * FROM usuario WHERE nombre = ?", (nombre,))
        datos = self.cursor.fetchone()
        if datos:
            _, nombre, tipo = datos
            if tipo == "cliente":
                return Cliente(nombre, tipo)
            elif tipo == "admin":
                return Admin(nombre, tipo)
        else:
            print("Usuario no encontrado.")
            return None

    def guardar_reserva(self, reserva):
        self.cursor.execute('''
            INSERT INTO reserva (nombre_cliente, fecha_entrada, fecha_salida, habitacion)
            VALUES (?, ?, ?, ?)
        ''', (reserva.cliente, reserva.entrada, reserva.salida, reserva.habitacion))
        self.conn.commit()

    def listar_reservas(self):
        self.cursor.execute("SELECT * FROM reserva")
        reservas = self.cursor.fetchall()
        for r in reservas:
            print(f"ID: {r[0]} - Cliente: {r[1]} - Entrada: {r[2]} - Salida: {r[3]} - Habitación: {r[4]} - Estado: {r[5]}")

    def cancelar_reserva(self, id_reserva):
        self.cursor.execute("UPDATE reserva SET estado = 'cancelada' WHERE id = ?", (id_reserva,))
        self.conn.commit()

# --------- EJECUCIÓN ---------

if __name__ == "__main__":
    sistema = SistemaReservas()

    # Cargar usuarios por única vez (solo si no existen)
    sistema.cursor.execute("SELECT COUNT(*) FROM usuario")
    if sistema.cursor.fetchone()[0] == 0:
        sistema.cursor.executemany('''
            INSERT INTO usuario (nombre, tipo) VALUES (?, ?)
        ''', [("Juan Cliente", "cliente"), ("Ana Admin", "admin")])
        sistema.conn.commit()

    usuario = sistema.login()

    if usuario:
        if isinstance(usuario, Cliente):
            usuario.hacer_reserva(sistema)
        elif isinstance(usuario, Admin):
            while True:
                print("\n1. Ver reservas\n2. Cancelar reserva\n3. Salir")
                op = input("Opción: ")
                if op == "1":
                    usuario.ver_reservas(sistema)
                elif op == "2":
                    usuario.cancelar_reserva(sistema)
                elif op == "3":
                    break
