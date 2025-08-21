import datetime

# Mostrar la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
print("Fecha y hora actual:", fecha_hora_actual)

# Pedir una fecha de entrega
fecha_entrega_str = input("Introduce la fecha de entrega (dd/mm/yyyy): ")
fecha_entrega = datetime.datetime.strptime(fecha_entrega_str, "%d/%m/%Y")

# Calcular cuántos días faltan para la entrega
dias_faltantes = (fecha_entrega - fecha_hora_actual).days

# Evaluar los días restantes y mostrar el mensaje correspondiente
if dias_faltantes > 7:
    print("Tenés bastante tiempo, ¡organizate bien!")
elif 1 <= dias_faltantes <= 7:
    print("La fecha se acerca, ponete las pilas")
elif dias_faltantes == 0:
    print("¡Hoy es el día de entrega!")
else:
    print("Ya te atrasaste en la entrega")

# Pedir la hora de estudio
hora_estudio = int(input("Introduce la hora de estudio (en formato 24h, por ejemplo 14 para las 14:00): "))

# Evaluar el horario de estudio
if 8 <= hora_estudio <= 20:
    print("Buen horario para estudiar")
else:
    print("Quizás es tarde, pensá en descansar")
