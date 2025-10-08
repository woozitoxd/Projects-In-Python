from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a Flask"

@app.route('/about')
def about():
    return "Esta es la página Acerca de"

if __name__ == '__main__':
    app.run(debug=True)
