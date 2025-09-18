notas = {
    "Juan": [7, 8, 9],
    "Ana": [10, 9, 8],
    "Luis": [6, 7, 5]
}

for alumno, lista_notas in notas.items():
    promedio = sum(lista_notas) / len(lista_notas)
    print(f"{alumno}: promedio = {promedio:.2f}")
