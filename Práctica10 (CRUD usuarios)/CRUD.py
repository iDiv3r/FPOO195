from Usuario import *

class CRUD:
    
    __usuarios = []
            
    def crearUsuario(self,usuario):
        self.__usuarios.append(usuario)
    
    def eliminarUsuario(self,nombre):
        for usuario in self.__usuarios:
            if usuario.getNombre() == nombre:
                self.__usuarios.remove(usuario)
    
    def editarUsuario(self, nombreB, atribN, atributo):
        for usuario in self.__usuarios:
            if usuario.getNombre() == nombreB:
                match atributo:
                    case 1:
                        usuario.setNombre(atribN)
                    case 2:
                        usuario.setCorreo(atribN)
                    case 3:
                        usuario.setContraseña(atribN)
                    case 4:
                        usuario.setEdad(atribN)
                    case _:
                        break
    
    def consultarUsuarios(self):
        return self.__usuarios
    
    def consultarUsuario(self, nombre):
        for usuario in self.__usuarios:
            if usuario.getNombre() == nombre:
                return usuario