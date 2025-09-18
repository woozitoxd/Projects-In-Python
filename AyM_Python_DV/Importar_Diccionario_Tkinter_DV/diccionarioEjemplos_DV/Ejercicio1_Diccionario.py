agenda = {}

agenda["Juan"] = "123456"
agenda["Ana"] = "789012"
agenda["Luis"] = "345678"

print("Agenda inicial:", agenda)

# Consultar un número
print("Teléfono de Ana:", agenda["Ana"])

# Eliminar un contacto
del agenda["Luis"]
print("Agenda actualizada:", agenda)
