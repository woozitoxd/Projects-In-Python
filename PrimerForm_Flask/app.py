from flask import Flask, render_template, request

app = Flask(__name__, template_folder='vistas')

@app.route('/')
def home():
    return render_template('formulario.html')


@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    return f'<h1>!Gracias! {nombre}! Te vamos a contactar al correo {correo}'

if __name__ == '__main__':
    app.run(debug=True)