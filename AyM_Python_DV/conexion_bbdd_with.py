import sqlite3

with sqlite3.connect("alumnos.db") as conexion:
    cursor = conexion.cursor()
    ## 
    # Resto del código a utilizar
    # (consultas, lógica, etc.)
    ##