nombreCompleto = input("Ingresa tu nombre completo: ")

#Forma 1
print(nombreCompleto.lower())
print(nombreCompleto.upper())
print(nombreCompleto.title())


#Forma 2
for i in range(3):
    if i==0:
        print(nombreCompleto.lower())
    elif i == 1:
        print(nombreCompleto.upper())
    elif i == 2:
        print(nombreCompleto.title())
                
                
#Forma 3

listaNombreCambiado = [nombreCompleto.lower(), nombreCompleto.upper(), nombreCompleto.title()]

for texto in listaNombreCambiado:
    print(texto)