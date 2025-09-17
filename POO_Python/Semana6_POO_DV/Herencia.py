class Persona:
    def __init__(self, nombre, edad):
        #Para crear atributos en Python se usa self.atributo, no es como en Java
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
        

class Estudiante(Persona): #La clase Estudiante hereda de la clase Persona
    def __init__(self, nombre, edad, curso):
        #Super en python es similar a Java, llama al constructor de la clase padre
        super().__init__(nombre, edad) 
        self.curso = curso

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.curso}.")
        
        
estudianteUno = Estudiante("Ghami", 30, "P.Avanzada")
estudianteUno.saludar()
estudianteUno.estudiar()
