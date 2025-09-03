from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# 1) Cuando un usuario se registra:
password = "mi_contraseña_segura123"
hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

print("Contraseña en texto plano:", password)
print("Contraseña encriptada (hash):", hashed_pw)


# Contraseña guardada (hash) en la base de datos
stored_pw = hashed_pw

# Contraseña que escribe el usuario en login
input_pw = "mi_contraseña_segura123"

if bcrypt.check_password_hash(stored_pw, input_pw):
    print("Login correcto")
else:
    print("Contraseña incorrecta")
