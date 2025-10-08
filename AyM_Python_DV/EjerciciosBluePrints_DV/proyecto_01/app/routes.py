from flask import Blueprint

main = Blueprint("main", __name__) #Creamos el blueprint

@main.route("/")
def home():
    return "Hola, esta es la página principal Da Vinci"

@main.route("/about")
def about():
    return "Acerca de nosotros"


