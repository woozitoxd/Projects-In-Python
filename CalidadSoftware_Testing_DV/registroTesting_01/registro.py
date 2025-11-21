def validar_registro(usuario, email, contraseña):
    """
    Valida los datos ingresados en un formulario de registro.
    Requisitos:
    - usuario no vacío
    - email contiene '@'
    - contraseña mínimo 6 caracteres
    """
    if not usuario:
        raise ValueError("El nombre de usuario no puede estar vacío.")
    if "@" not in email:
        raise ValueError("El email no es válido.")
    if len(contraseña) < 6:
        raise ValueError("La contraseña es demasiado corta.")
    return True
