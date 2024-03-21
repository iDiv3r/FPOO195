from Usuario import *
import sys 

class CajaPopular:
    
    __usuarios = []
    
    def crearUsuario(self,usuarioNuevo):
        i = 0
        for usuario in self.__usuarios:
            if usuario.getNumCuenta() == usuarioNuevo.getNumCuenta():
                i += 1
        
        if i == 0:
            self.__usuarios.append(usuarioNuevo)
            return 2
        else:
            return 1
    
    
    def consultarSaldo(self,numCuenta):
        for usuario in self.__usuarios:
            if usuario.getNumCuenta() == numCuenta:
                return usuario.getSaldo()
    
    
    def retirarEfectivo(self, numCuenta, retiro):
        for usuario in self.__usuarios:
            if usuario.getNumCuenta() == numCuenta:
                if usuario.getSaldo() > 0 and retiro <= usuario.getSaldo():
                    restante = (usuario.getSaldo() - retiro)
                    usuario.setSaldo(restante)
                    return 1
                    
                else:
                    return 2
    
    def depositarSaldo(self,origen,destino, cantidad):
        for usuario in self.__usuarios:
            if usuario.getNumCuenta() == origen:
                if usuario.getSaldo() > 0 and cantidad<= usuario.getSaldo():
                    restante = (usuario.getSaldo() - cantidad)
                    usuario.setSaldo(restante)

        for usuario in self.__usuarios:
            if usuario.getNumCuenta() == destino:
                restante = (usuario.getSaldo() + cantidad)
                usuario.setSaldo(restante)

    
    def ingresarSaldo(self,cuenta,cantidad):
        for usuario in self.__usuarios:
            if usuario.getNumCuenta() == cuenta:
                saldo = usuario.getSaldo() + cantidad
                usuario.setSaldo(saldo)
