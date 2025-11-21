import pytest
from registro import validar_registro

def test_registro_valido():
    assert validar_registro("florencia", "flor@correo.com", "abc123") is True

def test_usuario_vacio():
    with pytest.raises(ValueError):
        validar_registro("", "flor@correo.com", "abc123")

def test_email_invalido():
    with pytest.raises(ValueError):
        validar_registro("florencia", "florcorreo.com", "abc123")

def test_contraseña_corta():
    with pytest.raises(ValueError):
        validar_registro("florencia", "flor@correo.com", "123")
