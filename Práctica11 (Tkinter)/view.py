from tkinter import Tk, Frame, Button, messagebox


# Método para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinfo','Information'))
    print(messagebox.showerror('showerror','Error'))
    print(messagebox.showwarning('showwarning','Warning'))
    print(messagebox.askokcancel(message="¿Desea Continuar?"),title="Soy un titulo")

# Métodos 
def addbton():
    botonVerde.config(text="+")
    botonRosa = Button(seccion3,text='rosa', fg="black", bg="pink")
    botonRosa.configure(width='10',height='1')
    botonRosa.pack()







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


#3- Posicionar botones

# Place
botonAzul = Button(seccion1,text='azul', fg="darkblue")
botonAzul.place(x=60,y=60, width='100',height='30')

# Grid
botonNegro = Button(seccion2,text='negro', fg="#FFFFFF", bg="#000000")
botonNegro.configure(width='10',height='1')
botonNegro.grid(row=0,column=1)

botonAmarillo = Button(seccion2,text='amarillo', fg="black", bg="yellow", command=mostrarMensajes)
botonAmarillo.configure(width='10',height='1')
botonAmarillo.grid(row=2,column=2)

# Pack

botonVerde = Button(seccion3,text='verde', fg="black", bg="green",command=addbton)
botonVerde.configure(width='10',height='1')
botonVerde.pack()

botonVerde2 = Button(seccion3,text='verde2', fg="black", bg="lightgreen")
botonVerde2.configure(width='10',height='1')
botonVerde2.pack()







ventana.mainloop()
