from flask import Blueprint

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/')
def productos():
    return "Listado de usuarios"
