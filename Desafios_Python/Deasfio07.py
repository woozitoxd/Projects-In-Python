peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura: '))

IMC = peso / (altura)**2

numero_redondeado = round(IMC, 2)
print('Tu índice de masa corporal es ' + str(numero_redondeado))