# app.py
from flask import Flask, request, render_template, jsonify
from joblib import load
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # opcional: permite llamadas desde frontends desde otro lado (o Postman)

# Cargar el modelo una sola vez al iniciar la app (no por cada petición)
MODEL_PATH = "sentiment_model.joblib"
model = load(MODEL_PATH)

@app.route("/", methods=["GET"])
def index():
    # Muestra un formulario HTML simple (templates/index.html)
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Endpoint para el formulario (retorna HTML)
    text = request.form.get("text", "")
    if not text:
        return render_template("index.html", error="Ingresá un texto para analizar.")
    # predicción
    pred = model.predict([text])[0]                # etiqueta (ej: "positivo")
    probs = model.predict_proba([text])[0]         # probabilidades por clase
    classes = model.classes_                       # etiquetas según el modelo
    # preparar diccionario de probabilidades legible
    prob_dict = {cls: float(round(prob, 4)) for cls, prob in zip(classes, probs)} #Acá creo el diccionario de probabilidades
    return render_template("index.html", text=text, prediction=pred, probs=prob_dict)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    # Endpoint JSON (útil para Postman / fetch)
    data = request.get_json(force=True)
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Campo 'text' requerido"}), 400
    pred = model.predict([text])[0]
    probs = model.predict_proba([text])[0] #Proba es la lista de probabilidades
    classes = model.classes_
    prob_dict = {cls: float(round(prob, 4)) for cls, prob in zip(classes, probs)} 
    return jsonify({"text": text, "prediction": pred, "probabilities": prob_dict})

@app.route("/status", methods=["GET"]) 
def status():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)

