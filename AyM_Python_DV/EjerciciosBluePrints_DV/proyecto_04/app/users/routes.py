from flask import Blueprint, render_template

users = Blueprint("users", __name__, url_prefix="/users")

@users.route("/")
def users_list():
    lista_usuarios = ["Ana", "Luis", "María"]
    return render_template("users.html", usuarios=lista_usuarios)

@users.route("/<username>")
def user_profile(username):
    return f"Perfil de {username}"
