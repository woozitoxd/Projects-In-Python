def validar_edad(edad):
    """
    Verifica que la edad esté dentro de un rango válido (0–120).
    """
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120 años.")
    return True
