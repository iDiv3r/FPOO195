class Usuario:
    
    def __init__(self, nombre, correo, contraseña, edad):
        self.__nombre = nombre
        self.__correo = correo 
        self.__contraseña = contraseña 
        self.__edad = edad 
    
    # Gets
    def getNombre(self):
        return self.__nombre
    
    def getCorreo(self):
        return self.__correo
    
    def getContraseña(self):
        return self.__contraseña
    
    def getEdad(self):
        return self.__edad
    
    # Sets
    
    def setNombre(self,nombre):
        self.__nombre = nombre

    def setCorreo(self,correo):
        self.__correo =correo

    def setContraseña(self,contra):
        self.__contraseña = contra

    def setEdad(self,edad):
        self.__edad = edad

    
    
    