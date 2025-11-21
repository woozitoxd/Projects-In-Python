from auth import login

def test_login_exitoso():
    print("Probando login con credenciales correctas...")
    assert login("elias", "1234") is True, "El login debería funcionar con credenciales correctas"
    print("Login exitoso.")


def test_login_contraseña_incorrecta():
    assert login("elias", "xxxx") is False #Validamos que la contraseña incorrecta falle

def test_usuario_inexistente():
    assert login("pepito", "1234") is False #Validamos que un usuario inexistente falle
