# “Como usuario quiero buscar restaurantes por categoría para encontrar lo que quiero comer rápidamente.”

# Buscar Comida > Filtrar Nombre > Filtrar por Categoría > Filtrar por Precio > Ordenar por Precio > Ver Sugerencias
# Realizar Pedido > Seleccionar Plato > Llenar Datos (Formulario) > Agregar al Carrito (Quitar, Agregar) > Seleccionar tipo de Pago (Pagar) > 
# Hacer Seguimiento > Seleccionar tipo de Entrega > Ver tiempo estimado (Cancelar Pedido) > Ver ruta del envio >  


story_mapping = {
    "Buscar Comida": ["Filtrar Nombre", "Filtrar por Categoría", "Filtrar por Precio", "Ordenar por Precio"],
    "Realizar Pedido": ["Seleccionar Plato", " Llenar Datos (Formulario)", "Agregar al Carrito (Quitar, Agregar)", "Seleccionar tipo de pago"],
    "Hacer Seguimiento": ["Seleccionar tipo de Entrega", "Ver tiempo estimado (Cancelar Pedido)"]
}


def mostrarStoryMapping():
    contador = 0
    for actividad, funciones in story_mapping.items():
        print(f"Story Mapping {contador +1 }: Actividad: {actividad}")
        contador = contador +1
        for funcion in funciones:
            print(f"Tarea: {funcion}")
            
            
mostrarStoryMapping()
