class Persona:
    def __init__(self, nombre, edad):
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

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
        
p = Persona("Ana", 30)
print(p.get_nombre())  #Salida: Ana
p.set_nombre("Lucia")
print(p.get_nombre())  # Salida: Lucia


#Herencia

class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def estudiar(self):
        print(f"{self.nombre} está estudiando el curso {self.curso}.")
        
        
estudiante1 = Estudiante("Carlos", 20, "Matemáticas")
estudiante1.saludar()
estudiante1.estudiar()


#Polimorfismo


class Persona:
    def presentarse(self):
        print("Soy una persona.")

class Estudiante(Persona):
    def presentarse(self):
        print("Soy un estudiante.")
        
p = Persona()
e = Estudiante()
p.presentarse()  #Salida: Soy una persona.
e.presentarse()  # Salida: Soy un estudiante.