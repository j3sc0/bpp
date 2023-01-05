import tkinter as tk
from tkinter import ttk

"""
Crear la ventana principal del programa 
    .. Objeto ventana::

        >>> app=tk.Tk()
        >>> app.tittle("Tittle")
        >>> app.geometry("800x600")

    
"""
app = tk.Tk()
app.title("Mi aplicación de dibujo")
app.geometry("800x700")


"""
Crear el lienzo para dibujar
**Creamos la aplicación canvas donde ser va a poner los objetos**
empaquetamos el canvas en la ventana
"""
canvas = tk.Canvas(app, background="white", width=800, height=600)
canvas.pack()


"""
Crear la lista desplegable para seleccionar el color
"""
colors = ["red", "green", "blue"]
color_var = tk.StringVar(app)
color_var.set(colors[0])
color_select = ttk.Combobox(app, textvariable=color_var, values=colors)
color_select.pack()

"""
Crear la escala para seleccionar el grosor del lápiz
"""
pen_size = tk.Scale(app, from_=1, to=10, orient=tk.HORIZONTAL)
pen_size.pack()

"""
Función para dibujar líneas mientras se mantiene presionado el botón del ratón
"""
def draw(event):
    x, y = event.x, event.y
    canvas.create_line(x, y, x+1, y+1, width=pen_size.get(), fill=color_var.get())

canvas.bind("<B1-Motion>", draw)

"""
Función para borrar el dibujo
"""
def clear():
    canvas.delete("all")

"""
Crear el botón de borrado
"""
clear_button = tk.Button(app, text="Borrar", command=clear)
clear_button.pack()

"""
Mostrar la ventana
"""
app.mainloop()
