import tkinter as tk

def sumar():
    try:
        num1 = int(caja1.get())
        num2 = int(caja2.get())
        resultado.config(text=f"Resultado: {num1 + num2}")
    except ValueError:
        resultado.config(text="Por favor ingresa números")

ventana = tk.Tk()
ventana.title("Ejemplo Sumador Simple 2")
ventana.geometry("300x200")

tk.Label(ventana, text="Número 1").pack()
caja1 = tk.Entry(ventana)
caja1.pack()

tk.Label(ventana, text="Número 2").pack()
caja2 = tk.Entry(ventana)
caja2.pack()

boton = tk.Button(ventana, text="Sumar", command=sumar)
boton.pack()

resultado = tk.Label(ventana, text="Resultado:")
resultado.pack()

ventana.mainloop()
