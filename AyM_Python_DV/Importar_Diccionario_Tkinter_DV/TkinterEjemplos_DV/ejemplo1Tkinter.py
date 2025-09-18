import tkinter as tk

def saludar():
    etiqueta.config(text="¡Hola, mundo!")

ventana = tk.Tk()
ventana.title("Ejemplo 1")
ventana.geometry("300x200")
etiqueta = tk.Label(ventana, text="Pulsa el botón")
etiqueta.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

ventana.mainloop()
