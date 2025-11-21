def calcular_promedio(notas):
    if not notas:
        raise ValueError("La lista de notas está vacía.")
    promedio = sum(notas) / len(notas)
    #Error: la regla de negocio dice que aprueba con 6, pero usamos 7
    return "Aprobado" if promedio >= 7 else "Desaprobado"


#####
def calcular_promedio(notas):
    if not notas:
        raise ValueError("La lista de notas está vacía.")
    promedio = sum(notas) / len(notas)
    print(f"DEBUG: promedio calculado = {promedio}")
    return "Aprobado" if promedio >= 7 else "Desaprobado"


