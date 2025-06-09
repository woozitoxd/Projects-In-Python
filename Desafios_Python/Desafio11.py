inversionDepositada = float(input("Introduce la inversion: "))
intereses = 4 / 100 #4% de interes anual


for i in range(1, 4):
    balance = inversionDepositada * (1 + intereses) ** i #El interés compuesto implica que cada año se aplica el 4% sobre el total acumulado del año anterior
    print("Balance del año " + str(i) + " es de : " + str(round(balance, 2)))