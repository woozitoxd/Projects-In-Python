payaso = 112
muñeca = 75

cantidadPayasos = int(input('Ingrese cantidad de payasos vendidos: '))
cantidadMuñeca = int(input('Ingrese cantidad de muñecas vendidas: '))

pesoTotal = (cantidadMuñeca * muñeca) + (payaso * cantidadPayasos)

convertirKG = pesoTotal / 1000

print('El peso total del paquete a enviar es de : ' + str(round(convertirKG, 2)) + 'kg')