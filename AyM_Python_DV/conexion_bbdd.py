import sqlite3

conexion = sqlite3.connect("personas.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS personas (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)")
cursor.execute("INSERT INTO personas (nombre, edad) VALUES (?,?)", ("Messi", 31))
conexion.commit()

cursor.execute("SELECT * FROM personas")

for fila in cursor.fetchall():
    print(fila)
    
conexion.close()

conexion = sqlite3.connect("personas.db")
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS hijos (
    id_hijo INTEGER PRIMARY KEY,
    id_padre INTEGER,
    edad INTEGER,
    nombre TEXT,
    FOREIGN KEY (id_padre) REFERENCES personas (id)
)
""")
conexion.commit()


# Insertar un hijo para probar el INNER JOIN
cursor.execute("INSERT INTO hijos (id_padre, edad, nombre) VALUES (?, ?, ?)", (1, 5, "Thiago"))
conexion.commit()

# Consulta con INNER JOIN
cursor.execute("""
SELECT personas.nombre AS padre, hijos.nombre AS hijo, hijos.edad
FROM personas INNER JOIN hijos ON personas.id = hijos.id_padre
""")

for fila in cursor.fetchall():
    print("Join resultado:", fila)

conexion.close()
#FOREIGN KEY (group_id)
#      REFERENCES supplier_groups (group_id) 