class Usuario:
    
    __saldo = 0
    
    def __init__(self,numCuenta,titular,edad):
        self.__numCuenta = numCuenta 
        self.__titular = titular
        self.__edad = edad  
    
    # Gets
    
    def getNumCuenta(self):
        return self.__numCuenta

    def getTitular(self):
        return self.__titular

    def getEdad(self):
        return self.__edad

    def getSaldo(self):
        return self.__saldo

    # Sets
    
    def setNumCuenta(self,numCuenta):
        self.__numCuenta = numCuenta 

    def setTitular(self,titular):
        self.__titular = titular

    def setEdad(self,edad):
        self.__edad = edad

    def setSaldo(self,saldo):
        self.__saldo = saldo

    