class Persona:
    #declarar constructor y atributos

    def presentarse():
        print("Soy una persona.")
        
class Estudiante(Persona):
    def presentarse():
        print("Soy un estudiante.")

#Instanciamos los objetos
#En java sería Persona persona = new Persona();
#en python no se usa new porque el manejo de memoria es diferente
persona = Persona()
estudiante = Estudiante()

persona.presentarse()  #Salida: Soy una persona.
estudiante.presentarse()  # Salida: Soy un estudiante.
    