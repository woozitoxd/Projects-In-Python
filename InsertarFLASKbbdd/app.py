from flask import Flask, render_template, request
import sqlite3
import os


# Ruta absoluta a la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_BD = os.path.join(BASE_DIR, "db", "bbddLoginRegistro.db")
app = Flask(__name__, template_folder='vistas')

#Pagina Principal
@app.route('/')
def home():
    return render_template('registrarse.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['usuario']
        correo = request.form['correo']
        password = request.form['password']
        
        #Consultamos registro
        conexion = sqlite3.connect(RUTA_BD)
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND correo=? AND password=?", (nombre, correo, password))
        user = cursor.fetchone()
        conexion.close()
        
        if user:
            return render_template('index.html', nombre=nombre, correo=correo)
        else:
            return '<h2>Error: Credenciales incorrectas. </h2>'


#Registro Pagina
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']
        
        #guardar en mi base
        
        try:
            conexion = sqlite3.connect(RUTA_BD)
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO usuarios (nombre, correo, password) VALUES (?, ?, ?)',
                        (nombre, correo, password))
            conexion.commit()
            conexion.close()
            return render_template('login.html')
        except sqlite3.IntegrityError:
            return '<h2>Error: El correo ya existe. </h2>'
        
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)