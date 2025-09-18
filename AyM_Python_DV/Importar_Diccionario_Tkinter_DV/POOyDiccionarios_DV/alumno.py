class Alumno:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.materias = {}  # Diccionario: {"Matemática": [8, 9], "Historia": [7]}

    def agregar_nota(self, materia, nota):
        if materia not in self.materias:
            self.materias[materia] = []
        self.materias[materia].append(nota)

    def promedio(self):
        total_notas = 0
        cantidad = 0
        for notas in self.materias.values():
            total_notas += sum(notas)
            cantidad += len(notas)
        return total_notas / cantidad if cantidad > 0 else 0

    def mostrar_info(self):
        print(f"\nAlumno: {self.nombre} (DNI: {self.dni})")
        for materia, notas in self.materias.items():
            print(f"  {materia}: {notas}")
        print(f"Promedio general: {self.promedio():.2f}")
