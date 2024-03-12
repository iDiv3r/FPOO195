import random
import time

class Generador:
    
    def generarMatricula(self,nombre,apeP,apeM,añoN,carrera):
        
        añoCurso = "2024"
        
        charsAñoN = []
        charsAñoC = []
        
        matricula = ""
        
        
        for caracter in añoN:
            if caracter not in charsAñoN:
                charsAñoN.append(caracter)
        
        for caracter in añoCurso:
            if caracter not in charsAñoC:
                charsAñoC.append(caracter)
        
        
        matricula += random.choice(charsAñoC)
        matricula += random.choice(charsAñoC)
        matricula += random.choice(charsAñoN)
        matricula += random.choice(charsAñoN)
        matricula += nombre[:1]
        matricula += apeP[:1]
        matricula += apeM[:1]
        matricula += str(random.randint(1,9))
        matricula += str(random.randint(1,9))
        matricula += str(random.randint(1,9))
        matricula += carrera[:3]
        
        print(carrera[:3])
        return matricula