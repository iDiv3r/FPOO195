from tkinter import Tk, Frame, Button, messagebox, Label, Entry, ttk, Checkbutton, BooleanVar
from GeneradorPass import *

generador = GeneradorPass()

def generarCont(especiales , mayusculas,longitud):
    
    passNueva = generador.generarContraseña(especiales,mayusculas,longitud)
    
    print(messagebox.showinfo('Contraseña Nueva',("La nueva contraseña es:",passNueva)))
    
    txtNueva.delete(0,'end')
    txtNueva.insert(0,passNueva)
    

def validarContraseña(contraseña):
    validacion = generador.verificarContraseña(contraseña)
    
    match validacion:
        case 1:
            lblValidacion.config(text='La contraseña debil',bg='red')
            
        case 2:
            lblValidacion.config(text='La contraseña es decente',bg='yellow')
            
        case 3:
            lblValidacion.config(text='La contraseña es fuerte', bg='lightgreen')
        
        case 4:
            lblValidacion.config(text='La contraseña es muy fuerte', bg='green')
    

contraseña = Tk() 
contraseña.title('Generar Contraseñas')
contraseña.geometry('250x400')

fondo = Frame(contraseña,bg="white")
fondo.pack(expand=True,fill="both")

#-- 

lblLongitud = Label(fondo,text='Escribe la longitud',bg='white')
lblLongitud.place(x='10',y='60')

txtLongitud = Entry(fondo)
txtLongitud.configure(width='30')
txtLongitud.place(x='10',y='100')

#---
var1 = BooleanVar()
chkEspeciales = Checkbutton(fondo,text="Caracteres especiales",bg='white',variable=var1)
chkEspeciales.place(x='10',y='120')

#----

var2 = BooleanVar()
chkMayusculas = Checkbutton(fondo,text="Mayusculas",bg='white', variable=var2)
chkMayusculas.place(x='10',y='150')

#--

btnGenerar = Button(fondo,text="Crear contraseña",bg='lightgray',command=lambda: generarCont(var1.get(),var2.get(), int(txtLongitud.get().strip() or 8) ))
btnGenerar.configure(width='15',height='1')
btnGenerar.place(x='10',y='200')

#---

txtNueva = Entry(fondo)
txtNueva.configure(width='30')
txtNueva.place(x='10',y='240')

#---

btnValidar = Button(fondo,text="Validar contraseña",bg='lightgray',command=lambda: validarContraseña(txtNueva.get()))
btnValidar.configure(width='15',height='1')
btnValidar.place(x='10',y='270')

#--

lblValidacion = Label(fondo,bg='white')
lblValidacion.place(x='10',y='300')


contraseña.mainloop()