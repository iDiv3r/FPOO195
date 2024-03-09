import random
import string 

class GeneradorPass:
        
    def generarContraseña(self,especiales, mayusculas,longitud):
        
        letrasMinus = string.ascii_lowercase
        numeros = string.digits
        letrasMayus = string.ascii_uppercase
        caracteresEspeciales = string.punctuation
        
        contraseñaNueva = ""
        
        if especiales == False and mayusculas == False:
            i = 0
            while i < longitud:
                
                x =  random.randint(1,2)
                
                if x == 1:
                    contraseñaNueva += random.choice(letrasMinus)
                    i += 1
                    
                else:
                    contraseñaNueva += random.choice(numeros)
                    i += 1
            
            
        elif especiales == True and mayusculas == False:
            i = 0
            while i < longitud:
                
                x =  random.randint(1,3)
                
                if x == 1:
                    contraseñaNueva += random.choice(letrasMinus)
                    i += 1
                    
                elif x == 2:
                    contraseñaNueva += random.choice(numeros)
                    i += 1
                    
                else:
                    contraseñaNueva += random.choice(caracteresEspeciales)
                    i+= 1
            
            
        elif especiales == False and mayusculas == True:
            i = 0
            while i < longitud:
                
                x =  random.randint(1,3)
                
                if x == 1:
                    contraseñaNueva += random.choice(letrasMinus)
                    i += 1
                    
                elif x == 2:
                    contraseñaNueva += random.choice(numeros)
                    i += 1
                    
                else:
                    contraseñaNueva += random.choice(letrasMayus)
            
            
        elif especiales == True and mayusculas == True:
            i = 0
            while i < longitud:
                
                x =  random.randint(1,4)
                
                if x == 1:
                    contraseñaNueva += random.choice(letrasMinus)
                    i += 1
                    
                elif x == 2:
                    contraseñaNueva += random.choice(numeros)
                    i += 1
                    
                elif x == 3:
                    contraseñaNueva += random.choice(letrasMayus)
                    i += 1
                else:
                    contraseñaNueva += random.choice(caracteresEspeciales)
                    i += 1
        
        return contraseñaNueva