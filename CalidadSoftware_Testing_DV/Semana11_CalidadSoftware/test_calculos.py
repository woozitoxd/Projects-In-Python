#TestCalculo.py
from calculos import calcular_promedio
import pytest

def test_promedio_aprobado():
    assert calcular_promedio([8, 9, 7]) == "Aprobado"

def test_promedio_desaprobado():
    assert calcular_promedio([4, 1, 3]) == "Desaprobado"

def test_promedio_fuera_de_rango():
    with pytest.raises(ValueError):
        calcular_promedio([12, 8, 9])

