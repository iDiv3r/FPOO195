from tkinter import Tk, Frame, Button, messagebox, Label, Entry, ttk, Checkbutton, BooleanVar

from Generador import *

generador = Generador()

def generarMatricula(nombre,apeP,apeM,añoN,carrera):
    
    matriculaN = generador.generarMatricula(nombre,apeP,apeM,añoN,carrera)
    
    print(messagebox.showinfo('Nueva Matricula',"Tu nueva matrícula es: " + str(matriculaN)))


Interfaz = Tk() 
Interfaz.title('Generar Contraseñas')
Interfaz.geometry('250x700')

fondo = Frame(Interfaz,bg="white")
fondo.pack(expand=True,fill="both")

#-- 

lblNombre = Label(fondo,text='Escribe tu nombre',bg='white')
lblNombre.place(x='10',y='60')

txtNombre = Entry(fondo)
txtNombre.configure(width='30')
txtNombre.place(x='10',y='80')

#---

lblApellidoP= Label(fondo,text='Escribe tu apellido paterno',bg='white')
lblApellidoP.place(x='10',y='100')

txtApellidoP = Entry(fondo)
txtApellidoP.configure(width='30')
txtApellidoP.place(x='10',y='120')

#---

lblApellidoM= Label(fondo,text='Escribe tu apellido materno',bg='white')
lblApellidoM.place(x='10',y='140')

txtApellidoM = Entry(fondo)
txtApellidoM.configure(width='30')
txtApellidoM.place(x='10',y='160')

#---

lblNacimiento= Label(fondo,text='Escribe tu año de nacimiento',bg='white')
lblNacimiento.place(x='10',y='180')

txtNacimiento = Entry(fondo)
txtNacimiento.configure(width='30')
txtNacimiento.place(x='10',y='200')

#---

lblCarrera= Label(fondo,text='Escribe tu carrera',bg='white')
lblCarrera.place(x='10',y='220')

txtCarrera = Entry(fondo)
txtCarrera.configure(width='30')
txtCarrera.place(x='10',y='240')

#-------------------------

btnGenerar = Button(fondo,text="Crear contraseña",bg='lightgray',command=lambda: generarMatricula(txtNombre.get(),txtApellidoP.get(),txtApellidoM.get(),txtNacimiento.get(),txtCarrera.get()))
btnGenerar.configure(width='15',height='1')
btnGenerar.place(x='10',y='270')

#---

txtNueva = Entry(fondo)
txtNueva.configure(width='30')
txtNueva.place(x='10',y='240')



Interfaz.mainloop()