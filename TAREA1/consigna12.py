import datetime #Librería que nos permite trabajar con fechas y horas.


condicion1 = 0
condicion2 = 'a'

if condicion1:
    if condicion2:
        print("Ambas condiciones son verdaderas")
    else:
        print("Condición1 es verdadera pero condición2 es falsa")
else:
    print("Condición1 es falsa")


edad = 20
tiene_licencia = True

if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir.")
    else:
        print("Necesitas una licencia para conducir.")
else:
    print("Eres menor de edad. No puedes conducir.")


#Usando AND
edad = 22
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir legalmente.")
else:
    print("No cumples con los requisitos para conducir.")


#Usando OR
es_estudiante = True
es_jubilado = False

if es_estudiante or es_jubilado:
    print("Tienes derecho al descuento.")
else:
    print("No tienes descuento.")



#Utilizando fecha y hora:

import datetime

fechaHora = datetime.datetime.now()
print("Fecha y hora actual:", fechaHora)



#Utilizando solo la fecha

import datetime

fechaActual = datetime.date.today()
print("Fecha actual:", fechaActual)


#Creando fechas específicas

import datetime

fecha = datetime.date(2023, 8, 10)
print("Fecha específica:", fecha)

#Creando fechas específicas pero con hora
import datetime

fechaHora = datetime.datetime(2023, 8, 10, 15, 30, 0)
print("Fecha y hora específica:", fechaHora)



#Sumar días:

import datetime

fechaActual = datetime.date.today()
nuevaFecha = fechaActual + datetime.timedelta(days=10)
print("Fecha después de 10 días:", nuevaFecha)

#Restar días:

import datetime

fechaActual = datetime.date.today()
fechaPasada = fechaActual - datetime.timedelta(days=5)
print("Fecha hace 5 días:", fechaPasada)



#Parsear Fechas

import datetime

cadena = "10/08/2024"
fecha = datetime.datetime.strptime(cadena, "%d/%m/%Y")
print("Fecha parseada:", fecha)


#Comparación de Fechas
import datetime

fecha1 = datetime.date(2023, 8, 10)
fecha2 = datetime.date(2024, 8, 10)

if fecha1 < fecha2:
    print("fecha1 es anterior a fecha2")
else:
    print("fecha1 es igual o posterior a fecha2")
