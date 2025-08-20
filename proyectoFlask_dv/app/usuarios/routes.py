from flask import Blueprint

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
def lista():
    return "Listado de usuarios"
