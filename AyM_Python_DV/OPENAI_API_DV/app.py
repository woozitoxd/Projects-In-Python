# app.py
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargamos las variables que están guardadas en el archivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Permite que la API pueda ser usada desde otras aplicaciones (por ejemplo, el frontend)

# En lugar de usar un modelo entrenado localmente, ahora nos conectamos a la API de OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # La clave se toma automáticamente del .env
)

@app.route('/')
def index():
    # Mostramos la página principal
    return render_template('index.html')

@app.route("/api/predict", methods=['POST'])
def api_predict():
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({"error": "No se recibió ningún texto"}), 400

    try:
        # Acá pedimos a ChatGPT que analice el texto
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Se puede cambiar por "gpt-4o" si está disponible
            messages=[
                # Este mensaje le dice al modelo quién es y qué debe hacer
                {"role": "system", "content": "Eres un analista de sentimientos. Clasifica el texto como 'positivo', 'negativo' o 'neutral'."},
                
                # Este es el texto que envía el usuario para analizar
                {"role": "user", "content": text}
            ],
            temperature=0.1  # Mantiene las respuestas más consistentes y menos aleatorias
        )
        
        # Obtenemos la respuesta del modelo
        prediction = completion.choices[0].message.content.strip().lower()
        
        # Enviamos la respuesta en formato JSON
        return jsonify({
            "prediction": prediction,
            "text": text,
            "model_used": "gpt-3.5-turbo"
        })

    except Exception as e:
        # Si algo falla (por ejemplo, una API key incorrecta), devolvemos el error
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ejecuta la app en modo debug (útil durante el desarrollo)
    app.run(debug=True)
