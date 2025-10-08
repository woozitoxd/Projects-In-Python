from flask import Flask, render_template

app = Flask(__name__)

@app.route('/saludo/<usuario>')
def saludo(usuario):
    return render_template("saludo.html", usuario=usuario)

if __name__ == '__main__':
    app.run(debug=True)
