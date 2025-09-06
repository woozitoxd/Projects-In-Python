from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configurar LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Simulación de usuarios (trae de una BD)
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

# diccionario simulando la base de datos
users = {"elias": User(1, "elias")}

@login_manager.user_loader
def load_user(user_id):
    # Flask-Login necesita cargar el usuario desde la BD por ID
    for user in users.values():
        if str(user.id) == str(user_id):
            return user
    return None

@app.route("/login")
def login():
    user = users["elias"]
    login_user(user)  # Marca al usuario como logueado
    return f"Usuario {user.username} ha iniciado sesión"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Sesión cerrada"

@app.route("/perfil")
@login_required
def perfil():
    return f"Bienvenido {current_user.username} a tu perfil privado"
