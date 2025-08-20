import datetime
import locale

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")


# 1. Mostrar la fecha y hora actual
ahora = datetime.datetime.now()
print("Hoy es", ahora.strftime("%A, %d de %B de %Y, %H:%M hs"))

# 2. Pedir fecha de entrega
fecha_texto = input("Ingresá la fecha de entrega (dd/mm/yyyy): ")
fecha_entrega = datetime.datetime.strptime(fecha_texto, "%d/%m/%Y")

# 3. Calcular cuantos días faltan
diferencia = (fecha_entrega.date() - ahora.date()).days
print("Faltan", diferencia, "dias para la entrega.")

if diferencia > 7:
    print("Tenes bastante tiempo, ¡no procastines y organizate!")
elif 1 <= diferencia <= 7:
    print("La fecha se acerca, ponete las pilas")
elif diferencia == 0:
    print("¡Hoy es el día de entrega!")
else:
    print("Ya te atrasaste en la entrega")

# 4. Preguntar la hora actual de estudio
hora_estudio = int(input("Ingresá la hora actual (0-23): "))

if hora_estudio >= 8 and hora_estudio <= 20:
    print("Buen horario para estudiar")
else:
    print("Quizás es tarde, pensá en descansar")

# 5. (Opcional) Revisar día de la semana
dia_semana = ahora.strftime("%A")

if dia_semana == "sábado" or dia_semana == "domingo":
    print("Es fin de semana, descansa")
else:
    print("Es dia de semana, ponete a estudiar")
