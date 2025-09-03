from flask import Flask, request, jsonify, abort, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Base de datos SQLite en el archivo estudiantes.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudiantes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --------- Modelo ---------
class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    edad = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "edad": self.edad}

# --------- Inicialización de BD ---------
with app.app_context():
    db.create_all()

# --------- Helpers simples ---------
def validar_json_obligatorio(campos, data):
    if not data or not isinstance(data, dict):
        abort(400, description="Cuerpo JSON inválido.")
    faltantes = [c for c in campos if c not in data]
    if faltantes:
        abort(400, description=f"Faltan campos: {', '.join(faltantes)}")

def validar_estudiante_payload(data, parcial=False):
    # parcial=True permite PATCH (parcial)
    if not data or not isinstance(data, dict):
        abort(400, description="Cuerpo JSON inválido.")
    if not parcial:
        validar_json_obligatorio(["nombre", "edad"], data)
    if "nombre" in data and (not isinstance(data["nombre"], str) or not data["nombre"].strip()):
        abort(400, description="Campo 'nombre' debe ser texto no vacío.")
    if "edad" in data:
        try:
            edad = int(data["edad"])
            if edad < 0:
                abort(400, description="Campo 'edad' debe ser un entero >= 0.")
        except (TypeError, ValueError):
            abort(400, description="Campo 'edad' debe ser un entero.")

# --------- Rutas ---------
@app.route("/")
def home():
    return jsonify({"message": "API de Estudiantes - usa /estudiantes"}), 200



@app.route("/estudiantes", methods=["GET"])
def listar_estudiantes():
    ests = Estudiante.query.order_by(Estudiante.id).all()
    return jsonify([e.to_dict() for e in ests]), 200

@app.route("/estudiantes/<int:est_id>", methods=["GET"])
def obtener_estudiante(est_id):
    e = Estudiante.query.get_or_404(est_id, description="Estudiante no encontrado.")
    return jsonify(e.to_dict()), 200

@app.route("/estudiantes", methods=["POST"])
def crear_estudiante():
    data = request.get_json(silent=True)
    validar_estudiante_payload(data)
    e = Estudiante(nombre=data["nombre"].strip(), edad=int(data["edad"]))
    db.session.add(e)
    db.session.commit()
    # Location: URL del recurso creado
    return (
        jsonify(e.to_dict()),
        201,
        {"Location": url_for("obtener_estudiante", est_id=e.id, _external=True)},
    )

@app.route("/estudiantes/<int:est_id>", methods=["PUT"])
def reemplazar_estudiante(est_id):
    data = request.get_json(silent=True)
    validar_estudiante_payload(data)  # PUT requiere todo
    e = Estudiante.query.get_or_404(est_id, description="Estudiante no encontrado.")
    e.nombre = data["nombre"].strip()
    e.edad = int(data["edad"])
    db.session.commit()
    return jsonify(e.to_dict()), 200

@app.route("/estudiantes/<int:est_id>", methods=["PATCH"])
def actualizar_parcial(est_id):
    data = request.get_json(silent=True)
    validar_estudiante_payload(data, parcial=True)
    e = Estudiante.query.get_or_404(est_id, description="Estudiante no encontrado.")
    if "nombre" in data:
        e.nombre = data["nombre"].strip()
    if "edad" in data:
        e.edad = int(data["edad"])
    db.session.commit()
    return jsonify(e.to_dict()), 200

@app.route("/estudiantes/<int:est_id>", methods=["DELETE"])
def eliminar_estudiante(est_id):
    e = Estudiante.query.get_or_404(est_id, description="Estudiante no encontrado.")
    db.session.delete(e)
    db.session.commit()
    return "", 204

# --------- Manejo de errores JSON ---------
@app.errorhandler(400)
def bad_request(err):
    return jsonify(error="Bad Request", message=str(err.description)), 400

@app.errorhandler(404)
def not_found(err):
    return jsonify(error="Not Found", message=str(err.description)), 404

@app.errorhandler(500)
def server_error(err):
    return jsonify(error="Internal Server Error"), 500

if __name__ == "__main__":
    app.run(debug=True)
