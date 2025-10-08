from flask import Blueprint, jsonify, request
from models.database import get_db_connection

empleados_bp = Blueprint('empleados', __name__, url_prefix='/api/empleados')

# GET: Listar empleados
@empleados_bp.route("/", methods=["GET"])
def get_empleados():
    conn = get_db_connection()
    empleados = conn.execute("SELECT * FROM empleados").fetchall()
    conn.close()
    empleados_list = [dict(emp) for emp in empleados]
    return jsonify(empleados_list)

# GET individual
@empleados_bp.route("/<int:id>", methods=["GET"])
def get_empleado(id):
    conn = get_db_connection()
    emp = conn.execute("SELECT * FROM empleados WHERE id = ?", (id,)).fetchone()
    conn.close()
    if emp is None:
        return jsonify({"error": "Empleado no encontrado"}), 404
    return jsonify(dict(emp))

# POST: Agregar empleado
@empleados_bp.route("/", methods=["POST"])
def add_empleado():
    nuevo = request.get_json()
    nombre = nuevo.get("nombre")
    cargo = nuevo.get("cargo")
    salario = nuevo.get("salario")

    conn = get_db_connection()
    conn.execute("INSERT INTO empleados (nombre, cargo, salario) VALUES (?, ?, ?)",
                (nombre, cargo, salario))
    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Empleado agregado exitosamente"}), 201

# DELETE
@empleados_bp.route("/<int:id>", methods=["DELETE"])
def delete_empleado(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM empleados WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": f"Empleado con id {id} eliminado"})
