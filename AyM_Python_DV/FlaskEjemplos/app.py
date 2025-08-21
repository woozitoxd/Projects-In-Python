from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
@app.route('/index')  # También acepta /index
def home():
    return render_template('index.html')

# Ruta de saludo
@app.route('/saludo')
def saludo():
    return "Hola mundo desde otra ruta"

# Ruta de contacto
@app.route('/contacto')
def contacto():
    return "Página de contacto"

# Pasando datos a la plantilla
@app.route('/usuario')
def usuario():
    return render_template('usuario.html', nombre="Da Vinci")

if __name__ == '__main__':
    app.run(debug=True)
