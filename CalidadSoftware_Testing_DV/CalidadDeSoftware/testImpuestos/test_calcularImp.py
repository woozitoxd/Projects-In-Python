import pytest
from impuestos import calcular_impuesto

def test_impuesto_bajo():
    assert calcular_impuesto(9000) == 0 #Retorna 0 si el ingreso es menor o igual a 10000

def test_impuesto_medio():
    assert calcular_impuesto(20000) == 2000 #10% de 20000 es 2000, retorna 2000

def test_impuesto_alto():
    assert calcular_impuesto(100000) == 20000 #20% de 100000 es 20000, retorna 20000, si queremos mostrar el resultado en pantalla usamos print

def test_ingreso_negativo():
    with pytest.raises(ValueError): #Valida que se lance una excepción para ingreso negativo
        calcular_impuesto(-100)
