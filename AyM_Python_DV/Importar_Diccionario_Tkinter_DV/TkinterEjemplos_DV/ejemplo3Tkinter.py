import tkinter as tk

agenda = {}

def guardar_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    if nombre and telefono:
        agenda[nombre] = telefono
        etiqueta_resultado.config(text=f"Guardado: {nombre} -> {telefono}")
    else:
        etiqueta_resultado.config(text="Completa ambos campos")

ventana = tk.Tk()
ventana.title("Agenda con Tkinter")
ventana.geometry("300x200")
tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Teléfono:").pack()
entrada_telefono = tk.Entry(ventana)
entrada_telefono.pack()

boton = tk.Button(ventana, text="Guardar contacto", command=guardar_contacto)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
