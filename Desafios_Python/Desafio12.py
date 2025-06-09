panPrecio = 3.49

descuento = 60 / 100 # 60%
precioTotalDescuento = panPrecio * (1 - descuento) #Se aplica el descuento haciendo el precio del pan por el descuento -1

cant_panDeAyer = int(input("Ingrese la cantidad de barras de pan que no son del día de hoy: "))

print("El precio del pan es de: $", panPrecio)

print("El descuento por comprar pan de ayer es del: 60%")
print("Precio con descuento por undiad es de : $", round(precioTotalDescuento, 2)) #Redondeo 2 decimales

precioFinal = precioTotalDescuento * cant_panDeAyer #Se calcula el precio final multiplicando el descuento aplicado po la cantidad

print("El precio total por sus " + str(cant_panDeAyer) + " barras de pan de ayer, es de: $" +str(precioFinal))