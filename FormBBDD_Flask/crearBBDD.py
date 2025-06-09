import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #Usamos libreria OS para poder manejar las rutas de manera mas practica

carpeta_bd = os.path.join(BASE_DIR, "db") #Indicamos que cree la carpeta DB (este nombre podemos asignarlo el que querramos)
os.makedirs(carpeta_bd, exist_ok=True)

ruta_db = os.path.join(carpeta_bd, "baseDatosFLASK.db") #aca indicamos la ruta completa mas el nombre del archivo que querramos

conexion = sqlite3.connect(ruta_db) #a la conexion que crea la base de datos le pasamos la ruta que previamente indicamos
cursor = conexion.cursor()  #El cursor nos sirve para poder manejar la base de datos.

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, clave INTEGER)")
conexion.commit() #creamos la tabla


cursor.execute("INSERT INTO usuarios (nombre, clave) VALUES (?, ?)", ('admin', '1234'))

conexion.commit() #insertamos registro
conexion.close()
