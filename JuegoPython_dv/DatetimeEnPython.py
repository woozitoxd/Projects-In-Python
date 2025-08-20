import datetime

texto = "2025-08-19 21:30"
fecha = datetime.datetime.strptime(texto, "%Y-%m-%d %H:%M")
print("Fecha procesada:", fecha)

print("En texto:", fecha.strftime("%d de %B del %Y, %H:%M"))



fecha = datetime.datetime.today()
print("En texto:", fecha.strftime("%d de %B del %Y, %H:%M"))



hoy = datetime.datetime.today()
maniana = hoy + datetime.timedelta(days=1)
una_semana = hoy + datetime.timedelta(weeks=1)
hace_dos_horas = hoy - datetime.timedelta(hours=2)

print("Hoy:", hoy)
print("Mañana:", maniana)
print("Dentro de una semana:", una_semana)
print("Hace dos horas:", hace_dos_horas)


cadena = "03/20/2001"
fechaParseada = datetime.datetime.strptime(cadena, "%m/%d/%Y")
print(f"Cadena {cadena} que fue parseada a fecha: {fechaParseada}")

fechaFormateada = datetime.date(2001, 3, 20)

print(f"Fecha especificada es: {fechaFormateada}")


ahora = datetime.datetime.now()

fechaRestada = ahora / datetime.timedelta(days=7)

print(fechaRestada)

print(f"La fecha actual con horario es: {ahora}")
print(f"\n Deslogzado por Año, Mes, Día, Hora, Minuto y Segundo: \n")
print("Año:", ahora.year)
print("Mes:", ahora.month)
print("Día:", ahora.day)
print("Hora:", ahora.hour)
print("Minuto:", ahora.minute)
print("Segundo:", ahora.second)