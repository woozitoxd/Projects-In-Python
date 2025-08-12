from flask import Flask, url_for, render_template, request, redirect
from forms import SignupForm
app = Flask(__name__)  # Instancia de la clase WSGI, llamada APP
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

posts = []

@app.route('/')  # Route se encarga de decirle a FLASK qué URL debe ejecutar su correspondiente función
def index():
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)
    return render_template("index.html", num_post=len(posts))

@app.route("/p/<string:slug>/")  # El SLUG es una cadena de caracteres
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/")  # Crear post (arreglado con la barra inicial)
@app.route("/admin/post/<int:post_id>/")  # Modificar un post existente
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("singup_form.html", form=form)
    
# Estas líneas deben ir dentro de una función o ser llamadas en un entorno donde exista una aplicación activa (contexto de aplicación).
# Usar un bloque with si estamos en entorno de prueba:

with app.test_request_context():
    print(url_for("index"))  # /
    print(url_for("show_post", slug="leccion-1", preview=True))  # /p/leccion-1/?preview=True


if __name__ == "__main__":
    app.run(debug=True)
