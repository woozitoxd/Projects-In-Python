from flask import Flask, render_template

app = Flask(__name__)

usuarios = [
    {"nombre": "Ghami", "edad": 24},
    {"nombre": "Facundo", "edad": 27},
    {"nombre": "Elias", "edad": 24},
    {"nombre": "Carlos", "edad": 34}
]


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/usuarios')
def listar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
