inversion = float(input('¿Cuanto dinero va a invertir?: $ '))
interes_anual = float(input('Especifique el interes anual que corresponda: '))
anios = int(input('¿Por cuantos años será la inversión?: '))

ganancias = round((inversion * (interes_anual / 100 + 1) ** anios), 2)

print('Capital obtenido en la inversión: ' + str(ganancias))