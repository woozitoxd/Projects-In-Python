def calcular_promedio(notas):
    if not notas:
        raise ValueError("La lista de notas está vacía.")
    promedio = sum(notas) / len(notas)
    print(f"DEBUG: promedio calculado = {promedio}")
    return "Aprobado" if promedio >= 7 else "Desaprobado"


