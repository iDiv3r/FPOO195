class Personaje:
    # Atributo de personaje
    
    # Métodos del personaje --------
    
    # Crear método constructor
    def __init__(self, nombre, especie, altura):
        self.nombre = nombre
        self.especie = especie
        self.altura = altura
    
    
    def correr(self, estado):
        if(estado):
            print("El personaje",self.nombre, "está corriendo")
            
        else:
            print("El personaje",self.nombre, "está muerto")
            
            
    
    def lanzarGranada(self):
        print(self.nombre, "pegó una granada")
        
    

