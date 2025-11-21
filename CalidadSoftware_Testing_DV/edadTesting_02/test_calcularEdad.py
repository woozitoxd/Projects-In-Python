import pytest
from calcularEdad import validar_edad

def test_edad_valida():
    assert validar_edad(25) is True

def test_edad_fuera_de_rango():
    with pytest.raises(ValueError):
        validar_edad(130)

def test_edad_negativa():
    with pytest.raises(ValueError):
        validar_edad(-5)

def test_tipo_invalido():
    with pytest.raises(TypeError):
        validar_edad("veinte")
