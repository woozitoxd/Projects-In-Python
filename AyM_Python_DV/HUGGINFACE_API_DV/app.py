from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import requests # Usamos requests en lugar de openai
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

app = Flask(__name__)
CORS(app) # Opcional, pero útil

# --- Configuración de Hugging Face ---
HF_API_TOKEN = os.getenv("HF_API_TOKEN") # ¡Nuevo!
# Esta es la URL de la API para un modelo de análisis de sentimiento (clasificar texto positivo o negativo) popular
MODEL_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
# Preparamos los headers de autenticación
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# --- Ya no usamos el cliente de OpenAI ---
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def index():
    # Esto sigue exactamente igual
    return render_template('index.html')
@app.route("/api/predict", methods=['POST'])
def api_predict():
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        payload = {"inputs": text}
        response = requests.post(MODEL_URL, headers=HEADERS, json=payload)

        # --- ¡LÓGICA DE ERROR MEJORADA! ---
        if response.status_code != 200:
            error_message = f"Error de la API (Status {response.status_code})"
            
            # Intentamos leer el error como JSON (así vienen la mayoría)
            try:
                error_data = response.json()
                error_message = error_data.get("error", "Error desconocido en la API de HF")
                if "is currently loading" in error_message:
                    return jsonify({"error": "El modelo se está cargando, por favor intenta de nuevo en 20 segundos."}), 503
            except requests.exceptions.JSONDecodeError:
                # Si no es JSON (como un 404 o 500), solo usamos el texto.
                error_message = response.text 
            
            return jsonify({"error": error_message, "status_code": response.status_code}), response.status_code
        
        # --- Si llegamos aquí, todo salió bien (Status 200) ---
        prediction_data = response.json()
        
        predictions = prediction_data[0]
        best_prediction = max(predictions, key=lambda x: x['score'])
        
        # El modelo de roberta devuelve "LABEL_1", "LABEL_2", etc.
        # El de distilbert devuelve "POSITIVE", "NEGATIVE"
        # Hacemos el .lower() para normalizar
        prediction = best_prediction['label'].lower()
        
        return jsonify({
            "prediction": prediction,
            "text": text,
            "model_used": MODEL_URL.split('/')[-1]
        })

    except Exception as e:
        # Manejo de errores generales
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)