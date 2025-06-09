entero = int(input('Ingrese un numero entero divisor: '))
entero_dos = int(input('Ingrese un segundo numero entero dividendo: '))

cociente = entero / entero_dos

resto = entero % entero_dos


print(str(entero) + ' entre ' + str(entero_dos) + ' da un cociente de ' + str(int(cociente)) + ' y un resto de: ' + str(resto))