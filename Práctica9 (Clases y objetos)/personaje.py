class Personaje:
    # Atributo de personaje
    
    # Métodos del personaje --------
    
    # Crear método constructor
    def __init__(self, nombre, especie, altura):
        self.__nombre = nombre
        self.__especie = especie
        self.__altura = altura
    
    
    def correr(self, estado):
        if(estado):
            print("El personaje",self.__nombre, "está corriendo")
            
        else:
            print("El personaje",self.__nombre, "está muerto")
            
            
    
    def lanzarGranada(self):
        print(self.__nombre, "pegó una granada")
        
    
    # gets
    def getNombre(self):
        return self.__nombre

    def getEspecie(self):
        return self.__especie 
    
    def getAltura(self):
        return self.__altura
    
    # sets
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setEspecie(self, especie):
        self.__especie = especie
        
    def setAltura(self, altura):
        self.__altura = altura
        
    

    def __pensar(self):
        print(self.__nombre,"está pensando")