from tkinter import Tk, Frame, Button, messagebox, Label, Entry, ttk
from GeneradorPass import *

generador = GeneradorPass()

def generarCont(especiales , mayusculas,longitud):
    
    print (longitud)
    
    if especiales == "si":
        op1 = True
        
    else:
        op1 = False

    if mayusculas == "si":
        op2 = True
        
    else:
        op2 = False
        
    
    passNueva = generador.generarContraseña(op1,op2,longitud)
    
    print(messagebox.showinfo('Contraseña Nueva',("La nueva contraseña es:",passNueva)))
    
    txtNueva.delete(0,'end')
    txtNueva.insert(0,passNueva)
    
    

contraseña = Tk() 
contraseña.title('Ejemplo con 3 frames')
contraseña.geometry('600x600')

fondo = Frame(contraseña,bg="gray")
fondo.pack(expand=True,fill="both")

lblLongitud = Label(fondo,text='Escribe la longitud')
lblLongitud.place(x='250',y='50')

txtLongitud = Entry(fondo)
txtLongitud.configure(width='30')
txtLongitud.place(x='250',y='100')

#---

lblEspeciales = Label(fondo,text='¿Deseas caracteres especiales?')
lblEspeciales.place(x='250',y='150')

txtEspeciales = Entry(fondo )
txtEspeciales.configure(width='30')
txtEspeciales.place(x='250',y='200')

#----

lblMayusculas = Label(fondo,text='¿Deseas mayusculas?')
lblMayusculas.place(x='250',y='250')

txtMayusculas = Entry(fondo)
txtMayusculas.configure(width='30')
txtMayusculas.place(x='250',y='300')

#--

btnIngresar = Button(fondo,text="Ingresar",bg='blue',command=lambda: generarCont(txtEspeciales.get(),txtMayusculas.get(), int(txtLongitud.get().strip() or 8) ))
btnIngresar.configure(width='30',height='2')
btnIngresar.place(x='250',y='350')

#---

txtNueva = Entry(fondo)
txtNueva.configure(width='30')
txtNueva.place(x='250',y='450')

contraseña.mainloop()