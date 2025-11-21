from flask import Flask, request, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


app = Flask(__name__)
app.secret_key = "supersecretkey"

#Inicializamos Bcrypt y LoginManager
bcrypt = Bcrypt() 
login_manager = LoginManager()
login_manager.init_app(app) # Integrando con la app Flask


# Base de datos simulada
users = {}


class User(UserMixin): #Se usa UserMixin para facilitar la integración con Flask-Login
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash


@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(len(users) + 1, username, hashed_pw)
    users[user.id] = user
    return "Usuario registrado"


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    
    
    for user in users.values(): # Buscando usuario en la "base de datos"
        if user.username == username and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            return "Login exitoso"
    return "Usuario o contraseña incorrectos"

#En una base de datos real, se debería usar consultas para buscar el usuario.
#Ejemplo: user = User.query.filter_by(username=username).first()
# "query" es un atributo proporcionado por SQLAlchemy para realizar consultas en la base de datos.
# filter_by es un método que permite filtrar los resultados basándose en condiciones específicas, como el nombre de usuario en este caso.



@app.route("/perfil")
@login_required
def perfil():
    return f"Bienvenido {current_user.username}"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Sesión cerrada"



if __name__ == "__main__":
    app.run(debug=True)

