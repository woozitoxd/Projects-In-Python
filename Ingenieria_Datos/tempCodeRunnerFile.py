import csv
import sqlite3
import os
import datetime

def CrearTablaAlumnos(MiBase, archivo_log):
    
    try:
        
        conn = sqlite3.connect(MiBase)
        cursor = conn.cursor()

        lista_tablas = ['ID','Nombre', 'Apellido', 'Curso', 'Anio']
        # Recorro la lista,  creo las tablas en la BBDD e inserto los registros

        for tabla in lista_tablas:
            strDDLalumnos = 'CREATE TABLE IF NOT EXISTS "Alumnos" (ID INTEGER PRIMARY KEY, Nombre TEXT NOT NULL, Apellido TEXT NOT NULL, Curso TEXT NOT NULL, Anio INTEGER NOT NULL)'# creo la tabla donde vamos a insertar los registros
            cursor.execute(strDDLalumnos)
            
        RegistroEventosTXT(archivo_log, f"Se creo la tabla Alumnos")
        conn.commit()
        conn.close()
    except Exception as evento:
        print(f"Error: {str(evento)}")
        RegistroEventosTXT(archivo_log, f"Error: {str(evento)}")
        conn.commit()
        conn.close()
    
############################################################################################################################################################################

def CrearTablaCarrera(MiBase, archivo_log):
    
    try:
        conn = sqlite3.connect(MiBase)
        cursor = conn.cursor()
        
        lista_Tablas = ['IDCarrera', 'Carrera']
        
        for table in lista_Tablas:
            strDDLcarrera = 'CREATE TABLE IF NOT EXISTS "Carreras" (IDCarrera INTEGER PRIMARY KEY, Carrera TEXT NOT NULL)'
            cursor.execute(strDDLcarrera)
            
        RegistroEventosTXT(archivo_log, f"Se creo la tabla Carreras")
        conn.commit()
        conn.close()
    except Exception as evento:
        print(f"Error: {str(evento)}")
        RegistroEventosTXT(archivo_log, f"Error: {str(evento)}")
        conn.commit()
        conn.close()

############################################################################################################################################################################
def CrearTablaProfesores(MiBase, archivo_log):
    
    try:
        conn = sqlite3.connect(MiBase)
        cursor = conn.cursor()
        
        lista_Tablas = ['IDProfesor', 'Nombre', 'Apellido', 'Carrera']
        
        for table in lista_Tablas:
            strDDLcarrera = 'CREATE TABLE IF NOT EXISTS "Profesores" (IDProfesor INTEGER PRIMARY KEY NOT NULL, Nombre TEXT NOT NULL, Apellido TEXT NOT NULL, Carrera TEXT NOT NULL)'
            cursor.execute(strDDLcarrera)
            
        RegistroEventosTXT(archivo_log, f"Se creo la tabla PROFESORES")
        conn.commit()
        conn.close()
    except Exception as evento:
        print(f"Error: {str(evento)}")
        RegistroEventosTXT(archivo_log, f"Error: {str(evento)}")
        conn.commit()
        conn.close()
        
############################################################################################################################################################################
def CrearTablaNotasAlumnos(MiBase, archivo_log):
    
    try:
        
        conn = sqlite3.connect(MiBase)
        cursor = conn.cursor()

        lista_tablas = ['IDnota','IDalumno', 'IDAsignatura', 'Nota1', 'Nota2']
        # Recorro la lista,  creo las tablas en la BBDD e inserto los registros

        for tabla in lista_tablas:
            strDDLnotas = 'CREATE TABLE IF NOT EXISTS "Notas" (ID INTEGER PRIMARY KEY, Alumno TEXT NOT NULL, Asignatura TEXT NOT NULL, Nota1 INTEGER NOT NULL, Nota2 INTEGER NOT NULL)'# creo la tabla donde vamos a insertar los registros
            cursor.execute(strDDLnotas)
            
        RegistroEventosTXT(archivo_log, f"Se creo la tabla Notas")
        conn.commit()
        conn.close()
    except Exception as evento:
        print(f"Error: {str(evento)}")
        RegistroEventosTXT(archivo_log, f"Error: {str(evento)}")
        conn.commit()
        conn.close()

############################################################################################################################################################################

#Insercion de datos en la tabla alumnos
def InsertDatosAlumnos(miBaseAlumnos, ArchivoCSV, archivo_log):
    try:
        conn = sqlite3.connect(miBaseAlumnos)
        c = conn.cursor()        
        archivo = open(ArchivoCSV, 'r', encoding='utf-8')
        lista = csv.reader(archivo,delimiter=',')
        next(lista)
        
        for linea in lista:
            consultaSQL = "INSERT INTO ALUMNOS VALUES ('" + linea[0] + "','" + linea[1]  + "','" + linea[2] + "','" + linea[3] + "','"  + linea[4] +"')"
            c.execute(consultaSQL)
            conn.commit()
            RegistroEventosTXT(archivo_log, f"Se realizó la insercion en la tabla ALUMNOS")
            
        conn.close()
        print("Los datos del archivo CSV se insertaron correctamente")
    except Exception as evento:
        print(f"Error: {str(evento)}")
        RegistroEventosTXT(archivo_log, f"Error: {str(evento)}")
        conn.commit()
        conn.close()


    
############################################################################################################################################################################


#Insercion de datos en la tabla Carreras

def insertarDatosCarreras(miBaseCarrera, ArchivoCSV, archivo_log):
    try:
        conn = sqlite3.connect(miBaseCarrera)
        c = conn.cursor()        
        archivo = open(ArchivoCSV, 'r', encoding='utf-8')
        lista = csv.reader(archivo,delimiter=',')
        next(lista)
        
        for linea in lista:
            consultaSQL = "INSERT INTO CARRERAS VALUES ('" + linea[0] + "','" + linea[1]  + "')"
            c.execute(consultaSQL)
            conn.commit()
            RegistroEventosTXT(archivo_log, f"Se realizó la insercion en la tabla CARRERAS")
            
        conn.close()
        print("Los datos del archivo CSV se insertaron correctamente")
    except Exception as evento:
        print(f"Error: {str(evento)}")
        RegistroEventosTXT(archivo_log, f"Error: {str(evento)}")
        conn.commit()
        conn.close()
 
############################################################################################################################################################################
#Insercion de datos en la tabla Profesores
def insertarDatosProfesores(miBaseProfes, ArchivoCSV, archivo_log):
    try:
        conn = sqlite3.connect(miBaseProfes)
        c = conn.cursor()        
        archivo = open(ArchivoCSV, 'r', encoding='utf-8')
        lista = csv.reader(archivo,delimiter=',')
        next(lista)
        
        for linea in lista:
            consultaSQL = "INSERT INTO PROFESORES VALUES ('" + linea[0] + "','" + linea[1]  + "','" + linea[2] + "','" + linea[3] + "')"
            c.execute(consultaSQL)
            conn.commit()
            RegistroEventosTXT(archivo_log, f"Se realizó la insercion en la tabla PROFESORES")
            
        conn.close()
        print("Los datos del archivo CSV se insertaron correctamente")
    except Exception as evento:
        print(f"Error: {str(evento)}")
        RegistroEventosTXT(archivo_log, f"Error: {str(evento)}")
        conn.commit()
        conn.close()

 
############################################################################################################################################################################       
def InsertDatosNotasAlumnos(miBaseAlumnosNotas, ArchivoCSV, archivo_log):
    try:
        conn = sqlite3.connect(miBaseAlumnosNotas)
        c = conn.cursor()        
        archivo = open(ArchivoCSV, 'r', encoding='utf-8')
        lista = csv.reader(archivo,delimiter=',')
        next(lista)
        
        for linea in lista:
            consultaSQL = "INSERT INTO NOTAS VALUES ('" + linea[0] + "','" + linea[1]  + "','" + linea[2] + "','" + linea[3] + "','"  + linea[4] +"')"
            c.execute(consultaSQL)
            conn.commit()
            RegistroEventosTXT(archivo_log, f"Se realizó la insercion en la tabla NOTAS")
            
        conn.close()
        print("Los datos del archivo CSV se insertaron correctamente")
    except Exception as evento:
        print(f"Error: {str(evento)}")
        RegistroEventosTXT(archivo_log, f"Error: {str(evento)}")
        conn.commit()
        conn.close()


    
############################################################################################################################################################################

def RegistroEventosTXT(archivo_log, actividad):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = f"{timestamp} - {actividad}"
        
        with open(archivo_log, 'a') as log_file:
            log_file.write(registro + '\n')
            
    except Exception as evento:
        print(f"Error al registrar el evento: {str(evento)}")

############################################################################################################################################################################
        
if __name__ == "__main__":
    miBase = 'BBDDalumno.db'
    miArchivoAlumnos = os.getcwd() + '/TP_Integrador_INGdatos/alumnos.csv'
    miArchivoCarreras = os.getcwd() + '/TP_Integrador_INGdatos/carreras.csv'
    miArchivoProfesores = os.getcwd() + '/TP_Integrador_INGdatos/profesores.csv'
    miArchivoAlumnosNotas = os.getcwd() + '/TP_Integrador_INGdatos/NotasAlumnos.csv'
    archivo_log = "log.txt"
    
    CrearTablaAlumnos(miBase, archivo_log)
    CrearTablaCarrera(miBase, archivo_log)
    CrearTablaProfesores(miBase, archivo_log)
    CrearTablaNotasAlumnos(miBase, archivo_log)
    
    InsertDatosAlumnos(miBase, miArchivoAlumnos, archivo_log)
    insertarDatosCarreras(miBase, miArchivoCarreras, archivo_log)
    insertarDatosProfesores(miBase, miArchivoProfesores, archivo_log)
    InsertDatosNotasAlumnos(miBase, miArchivoAlumnosNotas, archivo_log)
        