personas = [{"nombre": "Juan", "edad": 25}, {"nombre": "Ana", "edad": 30}, {"nombre": "Pedro", "edad": 20}]
personas.sort(key=lambda x: x["edad"])
print(personas)  # [{"nombre": "Pedro", "edad": 20}, {"nombre": "Juan", "edad": 25}, {"nombre": "Ana", "edad": 30}]