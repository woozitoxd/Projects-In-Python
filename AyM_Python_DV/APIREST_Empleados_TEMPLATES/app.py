from flask import Flask, render_template, jsonify, request
from models import db, Empleado

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///empresa.db" # Base de datos 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.before_request
def crear_bd():
    db.create_all() #Esto crea las tablas si no existen

# Página de inicio
@app.route("/")
def inicio():
    return render_template("index.html")

# Mostrar empleados
@app.route("/empleados")
def mostrar_empleados():
    empleados = Empleado.query.all()
    return render_template("empleados.html", empleados=empleados)

# Formulario nuevo empleado
@app.route("/nuevo", methods=["GET", "POST"])
def nuevo_empleado():
    if request.method == "POST":
        nombre = request.form["nombre"]
        puesto = request.form["puesto"]
        salario = request.form["salario"]
        nuevo = Empleado(nombre=nombre, puesto=puesto, salario=salario)
        db.session.add(nuevo)
        db.session.commit()
        return render_template("confirmacion.html", mensaje="Empleado agregado con éxito.")
    return render_template("form_empleado.html")

# API REST endpoints
@app.route("/api/empleados", methods=["GET"])
def get_empleados():
    empleados = Empleado.query.all()
    resultado = [{"id": e.id, "nombre": e.nombre, "puesto": e.puesto, "salario": e.salario} for e in empleados]
    return jsonify(resultado), 200

@app.route("/api/empleados", methods=["POST"])
def add_empleado():
    nuevo = request.get_json()
    empleado = Empleado(nombre=nuevo.get("nombre"), puesto=nuevo.get("puesto"), salario=nuevo.get("salario"))
    db.session.add(empleado)
    db.session.commit()
    return jsonify({"mensaje": "Empleado agregado exitosamente"}), 201

@app.route("/api/empleados/<int:id>", methods=["GET"])
def get_empleado(id):
    empleado = Empleado.query.get(id)
    if empleado is None:
        return jsonify({"error": "Empleado no encontrado"}), 404
    return jsonify({"id": empleado.id, "nombre": empleado.nombre, "puesto": empleado.puesto, "salario": empleado.salario}), 200

@app.route("/api/empleados/<int:id>", methods=["PUT"])
def update_empleado(id):
    empleado = Empleado.query.get(id)
    if empleado is None:
        return jsonify({"error": "Empleado no encontrado"}), 404
    datos = request.get_json()
    empleado.nombre = datos.get("nombre", empleado.nombre)
    empleado.puesto = datos.get("puesto", empleado.puesto)
    empleado.salario = datos.get("salario", empleado.salario)
    db.session.commit()
    return jsonify({"mensaje": f"Empleado con id {id} actualizado"}), 200

@app.route("/api/empleados/<int:id>", methods=["DELETE"])
def delete_empleado(id):
    empleado = Empleado.query.get(id)
    if empleado is None:
        return jsonify({"error": "Empleado no encontrado"}), 404
    db.session.delete(empleado)
    db.session.commit()
    return jsonify({"mensaje": f"Empleado con id {id} eliminado"}), 200

if __name__ == "__main__":
    app.run(debug=True)
