import sqlite3

with sqlite3.connect("creacionBBDDflask.db") as conexion:
    cursor = conexion.cursor()
    ## 
    # Resto del código a utilizar
    # (consultas, lógica, etc.)
    ##