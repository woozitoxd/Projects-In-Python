#Usando App Factory

from flask import Flask

def create_app():
    app = Flask(__name__)

    from .usuarios.routes import usuarios_bp
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    
    from .productos.routes import productos_bp
    app.register_blueprint(productos_bp, url_prefix='/productos')

    return app
