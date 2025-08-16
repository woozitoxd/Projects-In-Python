#Paso importamos el modulo
import tkinter as tkin
from tkinter import messagebox


def saludar():
    print("Hola desde Tkinter")




def main():
    ventana = tkin.Tk()
    ventana.title("Mi Ventana Tkinter")
    ventana.geometry("300x200")
    
    etiqueta = tkin.Label(ventana, text="Hola, Tkinter")
    etiqueta.pack()  # Agrega el widget a la ventana
    
    boton = tkin.Button(ventana, text="Saludar", command=saludar)
    boton.pack() # Agregamos el boton a la ventana
    
    def mostrar_mensaje():
        messagebox.showinfo("Título", "Esto es una información")
        messagebox.showerror("Error", "Hubo un problema")
    
    
    boton = tkin.Button(ventana, text="Clic acá", command=mostrar_mensaje)
    boton.pack()
    
    entrada = tkin.Entry(ventana)
    entrada.pack() # Agregamos la entrada de texto a la ventana
    
    ventana.mainloop()
    
  
    
if __name__ == "__main__":
    main()


