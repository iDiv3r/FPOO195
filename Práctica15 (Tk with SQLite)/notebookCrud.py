from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

# Crear una nueva instancia de la clase controlador
controlador = Controlador()

def ejecutarInsert():
    controlador.insertarUsuario(nombreR.get(),correoR.get(),passwordR.get())
    

def buscarUsuario():
    resultado = controlador.buscarUsuario(idB.get())
    
    if (resultado == None or resultado == ""):
        messagebox.showwarning("Cuidado","No se encontró al usuario")

    else:
        resultadoB.delete("1.0",END)
        
        resultadoB.insert(END,"Id: " + str(resultado[0]) + "\n" + "Nombre: " + str(resultado[1]) + "\n" +"Correo: " + str(resultado[2]) + "\n" + "Contaseña: " + str(resultado[3]) + "\n")

def consultarUsuarios():
    consulta = controlador.consultarUsuarios()
    
    for item in tabla.get_children():
        tabla.delete(item)

    i = 0
    for usuario in consulta:
        tabla.insert("",'end',text=str(consulta[i][0],),values=(consulta[i][1],consulta[i][2],consulta[i][3]))
        i += 1
        

# 1- Crear la ventana 
Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("700x500")


# 2- Preparar el notebook para pestañas
panel = ttk.Notebook(Ventana)
panel.pack(fill='both',expand='yes')

# 3- Definir las pestañas del notebook
view1 = ttk.Frame(panel)
view2 = ttk.Frame(panel)
view3 = ttk.Frame(panel)
view4 = ttk.Frame(panel)
view5 = ttk.Frame(panel)

# 4- Añadir las pestañas
panel.add(view1,text="Crear Usuario")
panel.add(view2,text="Buscar usuario")
panel.add(view3,text="Consultar Usuarios")
panel.add(view4,text="Eliminar Usuario")
panel.add(view5,text="Editar Usuario")



# 5- Pestaña 1 (Crear Usuario)
Label(view1,text="Registro de usuarios",fg="Blue", font=("Papyrus",18)).pack()

nombreR = StringVar()
Label(view1,text="Nombre:").pack()
Entry(view1,textvariable=nombreR).pack()

correoR = StringVar()
Label(view1,text="Correo:").pack()
Entry(view1,textvariable=correoR).pack()

passwordR = StringVar()
Label(view1,text="Contraseña:").pack()
Entry(view1,textvariable=passwordR).pack()

Label(view1,text="").pack()

Button(view1,text="Guardar usuario",command=ejecutarInsert).pack()



# 6- Pestaña 2 (Formulario para consultar usuario)
Label(view2,text="Consultar usuario",fg="Blue", font=("Papyrus",18)).pack()

idB = IntVar()
Label(view2,text="Id:").pack()
Entry(view2,textvariable=idB).pack()

Label(view2,text="").pack()

Button(view2,text="Buscar usuario",command=buscarUsuario).pack()

Label(view2,text="Resultado").pack()
resultadoB = Text(view2,height=5,width=52)
resultadoB.pack()


# 7 - Pestaña 3 (Consultar usuarios)
Label(view3,text="Consultar Usuarios",fg="Blue", font=("Papyrus",18)).pack()

tabla = ttk.Treeview(view3,columns=("Nombre","Correo","Contraseña"))

tabla.column("#0",width=50)
tabla.column("Nombre",width=150)
tabla.column("Correo",width=150)

tabla.heading("#0",text="Id")
tabla.heading("Nombre",text="Nombre")
tabla.heading("Correo",text="Correo")
tabla.heading("Contraseña",text="Contraseña")


tabla.pack()

Label(view3,text="").pack()

boton = Button(view3,text="Consultar usuarios",command=consultarUsuarios).pack() 

Ventana.mainloop()