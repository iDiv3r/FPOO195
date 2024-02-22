class Personaje:
    # Atributo de personaje
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    # Métodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje",self.nombre, "está corriendo")
            
        else:
            print("El personaje",self.nombre, "está muerto")
            
            
    
    def lanzarGranada(self):
        print(self.nombre, "pegó una granada")
        
    
    def recargarArma(self, municion):
        cargador = 25
        cargador  += municion
        print("Arma recargada al", str(cargador), "%")
        
        


# Crear instancias del objeto personaje

spartan = Personaje()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

spartan.correr()
spartan.lanzarGranada()
spartan.recargarArma(50)