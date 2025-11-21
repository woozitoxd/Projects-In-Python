def calcular_impuesto(ingreso):
    """
    Calcula el impuesto anual según el ingreso:
    - Hasta 10000: 0%
    - 10001–50000: 10%
    - Más de 50000: 20%
    """
    if ingreso < 0:
        raise ValueError("El ingreso no puede ser negativo.") #Raise lanza una excepción si el ingreso es negativo
    if ingreso <= 10000:
        return 0 #Retorna 0 si el ingreso es menor o igual a 10000
    elif ingreso <= 50000:
        return ingreso * 0.10
    else:
        return ingreso * 0.20
