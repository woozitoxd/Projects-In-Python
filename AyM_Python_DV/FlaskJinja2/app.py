from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    usuarios = ['Da Vinci', 'Ghami', 'Elias', 'Facu', 'Sistema']
    return render_template('usuarios.html', usuarios=usuarios)


#Capturando Datos de un Formulario

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    return render_template('resultado.html', nombre=nombre, email=email)



if __name__ == '__main__':
    app.run(debug=True)

