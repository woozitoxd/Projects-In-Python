# train_model.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
# ------------ Datos de ejemplo -------------
# Un dataset muy pequeño para demo. Podemos usar un CSV con más filas si deseamos.
# Cada texto tiene una etiqueta: "positivo" o "negativo"
texts = [
    "me encanta esta clase",
    "esta materia es fantástica",
    "odio las tareas largas",
    "la clase fue aburrida",
    "excelente explicación",
    "no me gustó para nada",
    "muy interesante y didáctico",
    "pésima experiencia",
    "me gustó mucho el profesor",
    "no aprendí nada"
]
labels = [
    "positivo","positivo","negativo","negativo","positivo",
    "negativo","positivo","negativo","positivo","negativo"
]

# ------------- 2. Split entrenamiento / prueba -------------
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.25, random_state=42, stratify=labels
)

# ------------- 3. Pipeline: CountVectorizer + MultinomialNB -------------
pipeline = Pipeline([
    ("vect", CountVectorizer()),        # convierte texto a conteos (Bag of Words)
    ("clf", MultinomialNB())            # clasificador Naive Bayes multinomial
])

# ------------- 4. Entrenar -------------
pipeline.fit(X_train, y_train)

# ------------- 5. Evaluar (rápido) -------------
y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Reporte:\n", classification_report(y_test, y_pred))

# ------------- 6. Guardar el pipeline entrenado -------------
dump(pipeline, "sentiment_model.joblib")
print("Modelo guardado en sentiment_model.joblib")
