def calcular_promedio(notas):
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía.")
    promedio = sum(notas) / len(notas)
    #Error lógico intencional: aprueba con 7, cuando debería ser con 6
    return "Aprobado" if promedio >= 7 else "Desaprobado"