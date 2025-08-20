from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola a todos"

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/acerca')
def about():
    return "Acerca de nosotros"



#Parametros en URLs
@app.route('/usuario/<int:id>')
def perfil(id):
    return f"Perfil del usuario {id}"


#Busqueda en Flask con GET
@app.route('/buscar', methods=['GET'])
def buscar():
    consulta = request.args.get('q')  # Lee ?q=...
    return render_template('buscar.html', consulta=consulta)




#Formulario en Flask con POST
@app.route('/formulario')
def formulario():
    return render_template('form.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get('nombre')
    return f"Hola {nombre}, tus datos fueron recibidos."




#Manejo de Error 404
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
    


#Usando blueprint en flask
from flask import Blueprint

usuarios_bp = Blueprint('usuarios', __name__)
app.register_blueprint(app)

@usuarios_bp.route('/')
def lista():
    return "Listado de usuarios"

