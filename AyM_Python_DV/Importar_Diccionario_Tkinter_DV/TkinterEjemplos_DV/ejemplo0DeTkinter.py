
#Primer paso: importar la libreria
import tkinter as tkin
from tkinter import messagebox

def saludar(etiqueta):
    etiqueta.config(text="Hola desde Tkinter en la pantalla\n")
    print("Hola desde Tkinter en consola")

    
def main():
    ventana = tkin.Tk()
    ventana.title("Mi Ventana Tkinter")
    ventana.geometry("300x200")
    
    #Ahora usaremos algunos widgets
    etiqueta = tkin.Label(ventana, text="Hola, Tkinter")
    etiqueta.pack()  # Agrega el widget a la ventana
    
    boton = tkin.Button(ventana, text="Saludar", command=lambda: saludar(etiqueta))
    #Se utiliza lambda para pasar parametros a la funcion y que no se ejecute al crear el boton
    boton.pack() # Agregamos el boton a la ventana
    
    def mostrar_mensaje():
        messagebox.showinfo("Título", "Esto es una información")
        messagebox.showerror("Error", "Hubo un problema")
    
    
    boton = tkin.Button(ventana, text="Clic acá", command=mostrar_mensaje)
    boton.pack() # Agregamos el boton a la ventana
    
    entrada = tkin.Entry(ventana)
    entrada.pack() # Agregamos la entrada de texto a la ventana
    
    ventana.mainloop()# Inicia el loop de la ventana


if __name__ == "__main__":
    main()

