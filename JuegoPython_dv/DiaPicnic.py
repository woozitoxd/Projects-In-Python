# Mini-juego: ¿Hace un buen día para hacer picnic?

dia = input("Ingresa el día de la semana: ").lower()  # lunes, martes, etc.
llueve = input("¿Está lloviendo? (si/no): ").lower()
temperatura = int(input("¿Hace frío o calor, que temperatura hace? "))


# Regla: si no llueve, hay temperatura ideal entre 15 y 30°C, y no es lunes, se hace picnic

if llueve == "no" and 15 <= temperatura <= 30 and not dia == "lunes":
    print("¡Día de Picnic!")
elif llueve == "si" or temperatura < 15 or temperatura > 30:
    print("Mejor quedarse en casa viendo Netflix.")
else:
    print("Es lunes... :c")