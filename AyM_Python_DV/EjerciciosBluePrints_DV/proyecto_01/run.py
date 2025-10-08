from app import create_app

app = create_app() #Invocamos la función create_app para crear la instancia de la aplicación

if __name__ == "__main__":
    app.run(debug=True)
    
    