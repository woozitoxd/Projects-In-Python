from flask import Flask
from app.empleados.routes import empleados_bp

def create_app():
    app = Flask(__name__)

    # Importar y registrar los blueprints

    app.register_blueprint(empleados_bp)

    return app
