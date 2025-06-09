import sqlite3
from flask import Flask, render_template, request
import os


# Ruta absoluta a la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_BD = os.path.join(BASE_DIR, "db", "baseDatosFLASK.db")


app = Flask(__name__, template_folder='vistas')

#Pagina index
@app.route('/')
def index():
    return render_template('login.html')

#Procesa el login
@app.route('/login', methods=['POST'])
def login():
    
    usuario = request.form['usuario']
    clave = request.form['clave']
    
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND clave=?", (usuario, clave))
    user = cursor.fetchone()
    
    conexion.close()
    
    if user:
        return render_template('bienvenido.html', usuario=usuario)
    else:
        return 'Credenciales incorrectas. <a href="/">Intentar de nuevo </a>'
    
if __name__ == '__main__':
    app.run(debug=True)