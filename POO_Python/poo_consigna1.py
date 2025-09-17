class Persona:
    def __init__(self, nombre, edad):
        #Para crear atributos en Python se usa self.atributo, no es como en Java
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
        
        
        
persona1 = Persona("Ghami", 24)
persona1.saludar()
#Salida: Hola, me llamo Ghami y tengo 24 años


print(persona1.nombre) # Salida: Ghami
persona1.edad = 26
print(persona1.edad) # Salida: 26

##########################################
#Encapsulamiento Getters y Setters
class Persona:
    #El doble guion bajo hace que el atributo sea privado
    #Sin el guion bajo, el atributo es público
    #El atributo protegido se define con un solo guion bajo
    def __init__(self, nombre, edad):
        self.__nombre = nombre #público
        self.__apellido = nombre #privado
        self.__edad = edad #protegido

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
        
person = Persona("Elias", 30)
print(person.get_nombre())  #Salida: Elias
person.set_nombre("Ghami")
print(person.get_nombre())  # Salida: Ghami


#Herencia

class Estudiante(Persona): #La clase Estudiante hereda de la clase Persona
    def __init__(self, nombre, edad, curso):
        #Super en python es similar a Java, llama al constructor de la clase padre
        super().__init__(nombre, edad) 
        self.curso = curso

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.curso}.")
        
        
estudianteUno = Estudiante("Ghami", 3020, "P.Avanzada")
estudianteUno.saludar()
estudianteUno.estudiar()


#Polimorfismo


class Persona:
    def presentarse(self):
        print("Soy una persona.")

class Estudiante(Persona):
    def presentarse(self):
        print("Soy un estudiante.")
        
p = Persona() #Estamos asignando a una variable de tipo Persona un objeto de tipo Persona
e = Estudiante() #Estamos asignando a una variable de tipo Persona un objeto de tipo Estudiante
#Ahora llamamos al método presentarse de cada objeto
p.presentarse()  #Salida: Soy una persona.
e.presentarse()  # Salida: Soy un estudiante.