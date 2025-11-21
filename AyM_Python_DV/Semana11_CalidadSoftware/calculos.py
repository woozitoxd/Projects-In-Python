# calculos.py
def calcular_promedio(notas):
    if not notas:
        raise ValueError("Lista vacía")
    if any(n < 0 or n > 10 for n in notas):
        raise ValueError("Notas inválidas")
    promedio = sum(notas) / len(notas)
    return "Aprobado" if promedio >= 6 else "Desaprobado"