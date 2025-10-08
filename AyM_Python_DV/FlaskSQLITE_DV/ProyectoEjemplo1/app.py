from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection(): #Función para conectar a la base de datos que retorna la conexión
    conn = sqlite3.connect('empresa.db')
    conn.row_factory = sqlite3.Row #Acceder a las columnas por nombre con row_factory
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/empleados")
def empleados():
    conn = get_db_connection()
    empleados = conn.execute("SELECT * FROM empleados").fetchall()
    conn.close()
    return render_template("empleados.html", empleados=empleados)

if __name__ == "__main__":
    app.run(debug=True)
