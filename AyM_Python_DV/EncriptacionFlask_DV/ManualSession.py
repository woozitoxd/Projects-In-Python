from flask import Flask, session

app = Flask(__name__)
app.secret_key = "clave_muy_secreta"

@app.route("/set_session")
def set_session():
    session["user_id"] = 123
    return "Se guardó user_id en la sesión"

@app.route("/get_session")
def get_session():
    user_id = session.get("user_id")
    return f"El user_id en sesión es: {user_id}"

@app.route("/clear_session")
def clear_session():
    session.clear()
    return "Sesión borrada"

