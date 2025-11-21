import csv
import sqlite3
import os


#abrimos la base
conn = sqlite3.connect('clients.db')

c = conn.cursor()

carpeta = os.getcwd() + '/Ejemplos/'

#insertamos datos en las tablas

archivo = open(carpeta + 'Tipo.csv', 'r', encoding = 'utf-8')
lista = csv.reader(archivo, delimiter = ',')
next(lista)
for linea in lista:
    print(linea)
    strSQL = "INSERT INTO TIPO VALUES('" + linea[0] + "','" + linea[1] + "')"
    print(strSQL)
    conn.execute(strSQL)
    conn.commit() 

archivo.close()

archivo = open(carpeta + 'Provincia.csv', 'r', encoding = 'utf-8')
lista = csv.reader(archivo, delimiter = ',')
print(lista)
strSQL = "INSERT INTO Provincia (CODIGO, DESCRIPCION) VALUES(?, ?)"
c.executemany(strSQL,lista)
conn.commit() 
archivo.close()

archivo = open(carpeta + 'Localidad.csv', 'r', encoding = 'utf-8')
lista = csv.reader(archivo, delimiter = ',')
print(lista)

strSQL = "INSERT INTO Localidad (CODIGO, DESCRIPCION) VALUES(?, ?)"
c.executemany(strSQL,lista)
conn.commit() 
archivo.close()

#archivo = open(carpeta + 'Clientes.csv', 'r', encoding = 'utf-8')
#lista = csv.reader(archivo, delimiter = ',')
#print(lista)
#strSQL = "INSERT INTO Clientes (CODIGO, DESCRIPCION) VALUES(?, ?)"
#c.executemany(strSQL,lista)
#conn.commit() 
#archivo.close()

#Seleccionamos registros
select_all = "SELECT * FROM Localidad"
filas = c.execute(select_all).fetchall()

for fila in filas:
    print(fila)

#actualizar datos 

descripcion = 'Modificado'
codigo = 'BSAS'
c.execute(
    "UPDATE Provincia SET descripcion = ? WHERE codigo = ?",
    (descripcion, codigo)
)
conn.commit()
#Eliminar datos 

codigo = 'BSAS'
c.execute(
    "delete from Provincia WHERE codigo = ?",
    (codigo,)
)
conn.commit()


#Siempre cerrar todas las conexiones
c.close()
conn.close()