# Simulación de base de datos
usuarios = {
    "elias": "1234",
    "flor": "abcd",
} #Diccionario con usuarios y contraseñas

def login(usuario, contraseña): #Funcion para validar login
    """
    Valida usuario y contraseña.
    """
    if usuario not in usuarios:
        return False
    return usuarios[usuario] == contraseña #Retorna True si la contraseña es correcta, False en caso contrario
