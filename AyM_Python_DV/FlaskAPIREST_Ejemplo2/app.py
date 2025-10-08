from flask import Flask, jsonify, request
from models import database, Empleado

app = Flask(__name__)

# Configuración de base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///empresa.database"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database.init_app(app) #Esto es para inicializar la base de datos con la app de Flask


#ENDPOINT que devuelve todos los empleados
@app.route("/api/empleados", methods=["GET"])
def get_empleados():
    empleados = Empleado.query.all()
    resultado = [
        {"id": e.id, "nombre": e.nombre, "puesto": e.puesto, "salario": e.salario}
        for e in empleados
    ]
    return jsonify(resultado), 200

#ENDPOINT que añade un nuevo empleado
@app.route("/api/empleados", methods=["POST"])
def add_empleado():
    nuevo = request.get_json()
    empleado = Empleado(
        nombre=nuevo.get("nombre"),
        puesto=nuevo.get("puesto"),
        salario=nuevo.get("salario")
    )
    database.session.add(empleado)
    database.session.commit()
    return jsonify({"mensaje": "Empleado agregado exitosamente"}), 201

#ENDPOINT que actualiza un empleado por ID
@app.route("/api/empleados/<int:id>", methods=["PUT"])
def update_empleado(id):
    datos = request.get_json()
    empleado = Empleado.query.get(id)
    if not empleado:
        return jsonify({"mensaje": "Empleado no encontrado"}), 404

    empleado.nombre = datos.get("nombre", empleado.nombre)
    empleado.puesto = datos.get("puesto", empleado.puesto)
    empleado.salario = datos.get("salario", empleado.salario)

    database.session.commit()
    return jsonify({"mensaje": "Empleado actualizado exitosamente"}), 200

#ENDPOINT que elimina un empleado por ID
@app.route("/api/empleados/<int:id>", methods=["DELETE"])
def delete_empleado(id):
    empleado = Empleado.query.get(id)
    if empleado is None:
        return jsonify({"error": "Empleado no encontrado"}), 404

    database.session.delete(empleado)
    database.session.commit()
    return jsonify({"mensaje": f"Empleado con id {id} eliminado"}), 200


# Crear la base de datos si no existe
@app.before_request
def crear_bd():
    database.create_all()



if __name__ == "__main__": 
    app.run(debug=True)