from prueba_error_01 import calcular_promedio

def test_promedio_aprobado():
    resultado = calcular_promedio([8, 6, 7])
    assert resultado == "Aprobado", "El promedio debería aprobar con 6 o más"


