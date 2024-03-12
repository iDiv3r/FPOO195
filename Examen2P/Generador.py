import random

class Generador:
    
    def generarMatricula(self,nombre,apeP,apeM,añoN,carrera):
        
        añoCurso = "2024"
        
        matricula = ""
        
        matricula += (añoCurso[2:])
        matricula += (añoN[2:])
        matricula += nombre[:1]
        matricula += apeP[:1]
        matricula += apeM[:1]
        matricula += str(random.randint(1,9))
        matricula += str(random.randint(1,9))
        matricula += str(random.randint(1,9))
        matricula += str(carrera[:3])        
    
        
        return matricula