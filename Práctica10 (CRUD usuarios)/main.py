
from CRUD import *

app = CRUD()

while True:
    
    opcion = int(input('---------------------------------------------------------- \n Bienvenido al CRUD de usuarios, selecciona una opcion \n 1- Crear un usuario \n 2- Eliminar un usuario \n 3- Editar un usuario \n 4- Consultar todos los usuarios \n 5- Consultar usuario \n 6- Salir \n'))
    
    
    match opcion:
        case 1:
            nombre = str(input('Escriba el nombre del usuario \n'))
            correo = str(input('Escriba el correo del usuario \n'))
            contras = str(input('Escriba la contraseña del usuario \n'))
            edad = int(input('Escriba la edad del usuario \n'))
            
            usuarioNuevo = Usuario(nombre, correo, contras, edad)
            
            app.crearUsuario(usuarioNuevo)
            
            print('El usuario', nombre, 'ha sido creado con exito \n')
            
        case 2:
            nombreB = str(input('Escriba el nombre del usuario que desea eliminar \n'))
            
            app.eliminarUsuario(nombreB)
            
            print('El usuario', nombreB, 'ha sido eliminado con exito \n')
            
        case 3:
            nombreB = str(input('Escriba el nombre del usuario que desea modificar \n'))
            atributo = int(input('¿Que desea editar? \n 1- Nombre \n 2- Correo \n 3- Contraseña \n 4- Edad \n' ))
            match atributo:
                case 1:
                    atribN = str(input('Escriba el nuevo nombre \n'))
                case 2:
                    atribN = str(input('Escriba el nuevo correo \n'))
                case 3:
                    atribN = str(input('Escriba la nueva contraseña \n'))
                case 4:
                    atribN = int(input('Escriba la nueva edad \n'))
                case _:
                    print('error')
            
            app.editarUsuario(nombreB, atribN, atributo)
            
            print('Se ha actualizado el usuario', nombreB,'\n')
            
        case 4:
            usuarios = app.consultarUsuarios()
            
            for usuario in usuarios:
                print (usuario.getNombre(),'\n')
        
        case 5:
            nombreB = str(input('Escriba el nombre del usuario que desea consultar \n'))
            
            usuario = app.consultarUsuario(nombreB)
            
            print('Los datos del usuario son: \n Nombre:', usuario.getNombre(), '\n Correo:',usuario.getCorreo(),'\n Contraseña:', usuario.getContraseña(),'\n Edad:', usuario.getEdad(),'\n' )
            
        case 6:
            break
            
        case _:
            print('error')