from tkinter import messagebox
import sqlite3 
import bcrypt

class Controlador:
    
    def conexion(self):
        try:
            conex = sqlite3.connect("C:/Users/EMIga/OneDrive/Escritorio/5to cuatri/POO/FPOO195/Práctica15 (Tk with SQLite)/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    

    def encriptaPass(self, cont):
        passPlana = cont 
        passPlana = passPlana.encode()
        sal = bcrypt.gensalt()
        passHash = bcrypt.hashpw(passPlana,sal)
        
        return passHash


    def insertarUsuario(self,nombre,correo,contraseña):
        
        conexion = self.conexion()
        
        if(nombre == "" or correo == "" or contraseña == "" ):
            
            messagebox.showwarning("Cuidado","Inputs vacios")
            conexion.close()
            
        else:
            cursor = conexion.cursor()
            
            passwordH = self.encriptaPass(contraseña)
            
            datos = (nombre,correo,passwordH)
            
            sqlInsert = 'INSERT INTO tbUsuarios(nombre,correo,password) values (?,?,?)'
            
            cursor.execute(sqlInsert,datos) 
            
            conexion.commit()
            conexion.close()
            
            messagebox.showinfo("Exito","Un nuevo papu apareció en papulandia.")
    
    
    
    def buscarUsuario(self,id):
        conexion = self.conexion()
        
        if id <= 0 :
            
            messagebox.showwarning("Cuidado","Introduzca un id válido.")
            conexion.close()
            
        else:
            try:
                cursor = conexion.cursor()
                
                sqlInsert = 'select * from tbUsuarios where id = ' + str(id)
                
                cursor.execute(sqlInsert) 
                
                datos = cursor.fetchall()
                
                conexion.close()
                
                return datos

            except sqlite3.OperationalError:
                print("Error en la búsqueda")