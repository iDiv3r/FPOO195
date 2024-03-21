from tkinter import Tk, Frame, Button, messagebox, Label, Entry, ttk, Checkbutton, BooleanVar
from CajaPopular import *

cajaP = CajaPopular()

caja = Tk() 
caja.title('Generar Contraseñas')
caja.geometry('300x800')

fondo = Frame(caja,bg="white")
fondo.pack(expand=True,fill="both")

# ----------------------------

def crearUsuario(numeroCuenta,titular,edad):
    
    usuarioNuevo = Usuario(numeroCuenta,titular,edad)
    
    v = cajaP.crearUsuario(usuarioNuevo)
    
    match v:
        case 1:
            print(messagebox.showerror("Error","El usuario ingresado ya existe"))
        case 2:
            print(messagebox.showinfo("Bienvenido","El usuario fue creado con exito"))
    

def consultarSaldoUsuario(numCuenta):

    saldo = cajaP.consultarSaldo(numCuenta)
    
    print(messagebox.showinfo("Saldo","El saldo de la cuenta " + str(numCuenta) + " es: " + str(saldo)))
    
    lblResultadoCons.config(text="El saldo es " + str(saldo))
    

def retirarEfectivoUsuario(numCuenta,retiro):
    
    x = cajaP.retirarEfectivo(numCuenta,retiro)
    
    match x:
        case 1:
            print(messagebox.showinfo("Retirar","Se han retirado " + str(retiro) + " de la cuenta " + str(numCuenta)))
            
        case 2:
            print(messagebox.showerror("Error","Saldo Insuficiente"))

def depositarSaldoUsuario(origen,destino,cantidad):
    
    x = cajaP.depositarSaldo(origen,destino,cantidad)
    
    print(messagebox.showinfo("Depositar","Se han depositado " + str(cantidad) + " de la cuenta " + str(origen) + " a la cuenta " + str(destino)))
    

def ingresarSaldoUsuario(cuenta,cantidad):
    
    cajaP.ingresarSaldo(cuenta,cantidad)
    
    print(messagebox.showinfo("Exito","Se depositaron " + str(cantidad) + " a la cuenta " + str(cuenta))) 


# ----------------------------

# crear usuario

lblNumero = Label(fondo,text='Escribe el numero de cuenta',bg='white')
lblNumero.place(x='10',y='30')

txtNumero = Entry(fondo)
txtNumero.configure(width='30')
txtNumero.place(x='10',y='50')

lblTitular = Label(fondo,text='Escribe el titular de cuenta',bg='white')
lblTitular.place(x='10',y='80')

txtTitular = Entry(fondo)
txtTitular.configure(width='30')
txtTitular.place(x='10',y='100')

lblEdad = Label(fondo,text='Escribe la edad del titular',bg='white')
lblEdad.place(x='10',y='130')

txtEdad = Entry(fondo)
txtEdad.configure(width='30')
txtEdad.place(x='10',y='150')

btnAccion  = Button(fondo,text="Crear",bg='lightgray',command=lambda: crearUsuario(int(txtNumero.get()), txtTitular.get(),int(txtEdad.get())))
btnAccion.configure(width='15',height='1')
btnAccion.place(x='10',y='180')


# consultar

lblConsultar = Label(fondo,text='Escribe el numero de cuenta que quieres consultar',bg='white')
lblConsultar.place(x='10',y='230')

txtConsultar = Entry(fondo)
txtConsultar.configure(width='30')
txtConsultar.place(x='10',y='250')

btnConsultar  = Button(fondo,text="Consultar",bg='lightgray',command=lambda: consultarSaldoUsuario(int(txtConsultar.get())))
btnConsultar.configure(width='15',height='1')
btnConsultar .place(x='10',y='280')

lblResultadoCons = Label(fondo,bg='white')
lblResultadoCons.place(x='10',y='310')


# ingresar y retirar efectivo   

lblAccion = Label(fondo,text='Escribe tu cuenta',bg='white')
lblAccion.place(x='10',y='360')

txtAccion = Entry(fondo)
txtAccion.configure(width='30')
txtAccion.place(x='10',y='380')

lblCantidad = Label(fondo,text='Escribe la cantidad',bg='white')
lblCantidad.place(x='10',y='410')

txtCantidad = Entry(fondo)
txtCantidad.configure(width='30')
txtCantidad.place(x='10',y='440')

btnRetirar = Button(fondo,text="Retirar",bg='lightgray',command=lambda: retirarEfectivoUsuario(int(txtAccion.get()),float(txtCantidad.get())))
btnRetirar.configure(width='15',height='1')
btnRetirar.place(x='10',y='470')

btnIngresar = Button(fondo,text="Ingresar",bg='lightgray', command=lambda: ingresarSaldoUsuario(int(txtAccion.get()),float(txtCantidad.get())))
btnIngresar.configure(width='15',height='1')
btnIngresar.place(x='150',y='470')

# depositar a otra cuenta

lblDepositar1 = Label(fondo,text='Escribe la cuenta de origen',bg='white')
lblDepositar1.place(x='10',y='520')

txtDepositar1 = Entry(fondo)
txtDepositar1.configure(width='30')
txtDepositar1.place(x='10',y='540')

lblDepositar2 = Label(fondo,text='Escribe la cuenta de destino',bg='white')
lblDepositar2.place(x='10',y='570')

txtDepositar2 = Entry(fondo)
txtDepositar2.configure(width='30')
txtDepositar2.place(x='10',y='590')

lblCantidadRet = Label(fondo,text='Escribe la cantidad a depositar',bg='white')
lblCantidadRet.place(x='10',y='620')

txtCantidadRet = Entry(fondo)
txtCantidadRet.configure(width='30')
txtCantidadRet.place(x='10',y='640')

btnDepositar  = Button(fondo,text="Depositar",bg='lightgray',command= lambda: depositarSaldoUsuario(int(txtDepositar1.get()),int(txtDepositar2.get()),float(txtCantidadRet.get())))
btnDepositar.configure(width='15',height='1')
btnDepositar.place(x='10',y='670')


caja.mainloop()