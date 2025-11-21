from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('empresa.db')
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint GET: listar empleados
@app.route("/api/empleados", methods=["GET"])
def get_empleados():
    conn = get_db_connection()
    empleados = conn.execute("SELECT * FROM empleados").fetchall()
    conn.close()
    return jsonify([dict(emp) for emp in empleados])

# Endpoint POST: crear empleado
@app.route("/api/empleados", methods=["POST"])
def add_empleado():
    nuevo = request.get_json()
    conn = get_db_connection()
    conn.execute("INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)", 
                (nuevo.get("nombre"), nuevo.get("puesto"), nuevo.get("salario")))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Empleado agregado exitosamente"}), 201


# Endpoint PUT: actualizar empleado
@app.route("/api/empleados/<int:id>", methods=["PUT"])
def update_empleado(id):
    datos = request.get_json()
    conn = get_db_connection()
    conn.execute("UPDATE empleados SET nombre = ?, puesto = ?, salario = ? WHERE id = ?", 
                (datos.get("nombre"), datos.get("puesto"), datos.get("salario"), id))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": f"Empleado con id {id} actualizado"})

# Endpoint GET individual
@app.route("/api/empleados/<int:id>", methods=["GET"])
def get_empleado(id):
    conn = get_db_connection()
    emp = conn.execute("SELECT * FROM empleados WHERE id = ?", (id,)).fetchone()
    conn.close()
    if emp is None:
        return jsonify({"error": "Empleado no encontrado"}), 404
    return jsonify(dict(emp))

# Endpoint DELETE
@app.route("/api/empleados/<int:id>", methods=["DELETE"])
def delete_empleado(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM empleados WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": f"Empleado con id {id} eliminado"})

if __name__ == "__main__":
    app.run(debug=True)