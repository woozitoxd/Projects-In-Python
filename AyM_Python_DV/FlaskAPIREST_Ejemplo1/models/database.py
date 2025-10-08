from flask import Flask
import sqlite3

app = Flask(__name__)

# ---------------------------
# Conexión a la base de datos
# ---------------------------
def get_db_connection():
    conn = sqlite3.connect('empresa.db')
    conn.row_factory = sqlite3.Row
    return conn
