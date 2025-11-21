from flask_bcrypt import Bcrypt

#Veremos un ejemplo sencillo sobre cómo usar Flask-Bcrypt para hashear contraseñas en una aplicación Flask.

bcrypt = Bcrypt()

# Ejemplo de uso
password = "Mi_Contraseña_DaVinci"

hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') # Hasheando la 

print(f"Contraseña original: {password}")
print(f"Contraseña hasheada: {hashed_password}")

#Simulando verificación
#Contraseña guardada en la base de datos (hasheada)
stored_hashed_password = hashed_password  # Simulando que esta es la contraseña guardada
# Contraseña ingresada por el usuario para verificar
user_input_password = "Mi_Contraseña_DaVinci"

if bcrypt.check_password_hash(stored_hashed_password, user_input_password):
    print("Acceso concedido")
else:
    print("Acceso denegado")