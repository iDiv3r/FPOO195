from tkinter import Tk, Frame

# 1- Crear la ventana 

ventana = Tk() # Crear una instancia de tk

ventana.title('Ejemplo con 3 frames')

ventana.geometry('600x400')


# 2- Colocar las secciones de la ventana

seccion1 = Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')

seccion2 = Frame(ventana,bg="white")
seccion2.pack(expand=True,fill='both')

seccion3 = Frame(ventana,bg="green")
seccion3.pack(expand=True,fill='both')





ventana.mainloop()
