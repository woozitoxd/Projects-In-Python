import datetime
import locale
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

# Mostrar fecha y hora actual
ahora = datetime.datetime.now()
print("Hoy es", ahora.strftime("%A, %d de %B de %Y, %H:%M hs"))

# Pedir fecha de entrega
fecha_str = input("Ingresá la fecha de entrega (dd/mm/yyyy): ")
fecha_entrega = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")

# Calcular días restantes
dias_faltan = (fecha_entrega - ahora).days

# Mensajes según días faltantes
if dias_faltan > 7:
    print("Tenés bastante tiempo, ¡organizate bien!")
elif 1 <= dias_faltan <= 7:
    print("La fecha se acerca, ponete las pilas")
elif dias_faltan == 0:
    print("¡Hoy es el día de entrega!")
else:
    print("Ya te atrasaste en la entrega")

# Pedir hora de estudio
hora_estudio = int(input("Ingresá la hora actual de estudio (0-23): "))
if 8 <= hora_estudio <= 20:
    print("Buen horario para estudiar")
else:
    print("Quizás es tarde, pensá en descansar")
