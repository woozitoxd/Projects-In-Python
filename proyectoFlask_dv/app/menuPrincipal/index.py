from flask import Blueprint, render_template

indice = Blueprint('index', __name__)

@indice.route('/')
def index():
    return render_template('index.html')