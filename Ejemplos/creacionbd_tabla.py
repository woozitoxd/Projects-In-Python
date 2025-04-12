#importar la libreria

import sqlite3

# Nos conectamos a la BD
# Si existe la abrimos
# Sino la creamos 

conn = sqlite3.connect('clientes.db')

#Generamos un cursor
#Pasamos la cadena DDL
#Creamos una tabla

c = conn.cursor()

# creo la tabla donde vamos a insertar los registros

#strDDL = 'CREATE TABLE "Cliente" ("CODCLI"	INTEGER NOT NULL,"APYNOM"	TEXT NOT NULL,	"TIPO"	TEXT,"COD_IVA"	TEXT,"CALLE"	TEXT,	"NRO"	TEXT,	"NRO_MED"	TEXT,	"PISO"	TEXT, "DEPT"	TEXT,	"COD_POSTAL"	TEXT,	"COD_LOC"	TEXT,	"COD_PROV"	TEXT,	"TELEFONOS"	TEXT,	"EMAIL"	TEXT,	"FECHA_ALTA"	TEXT,	"FECHA_BAJA"	TEXT,	"TIPO_DOC"	TEXT,	"NRO_DOC"	TEXT, PRIMARY KEY("CODCLI"));'
#c.execute(strDDL)

lista_tablas = ['Localidad', 'Provincia', 'Tipo']

# Recorro la lista,  creo las tablas en la BBDD e inserto los registros

for tabla in lista_tablas:
    strDDL = 'CREATE TABLE "' + tabla + '" ( "CODIGO" TEXT NOT NULL,"DESCRIPCION" TEXT NOT NULL);'
    c.execute(strDDL)

conn.commit()

strDML = 'select * from Cliente'
registros = c.execute(strDML).fetchall()
print(registros)
c.close()
conn.close()