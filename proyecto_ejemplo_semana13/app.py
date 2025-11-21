# app.py
from flask import Flask
from dotenv import load_dotenv
import os

# Cargar las variables desde .env
load_dotenv()

app = Flask(__name__)

# Usar las variables de entorno
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

@app.route('/')
def home():
    return f"Conectado a: {app.config['DATABASE_URL']}"

if __name__ == '__main__':
    app.run(debug=True)
