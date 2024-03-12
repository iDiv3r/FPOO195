import random
import string 

class GeneradorPass:
    
    letrasMinus = string.ascii_lowercase
    numeros = string.digits
    letrasMayus = string.ascii_uppercase
    caracteresEspeciales = string.punctuation   
    

    def generarContraseña(self,especiales, mayusculas,longitud):
        
        contraseñaNueva = ""
        
        if especiales == False and mayusculas == False:
            i = 0
            while i < longitud:
                
                x =  random.randint(1,2)
                
                if x == 1:
                    contraseñaNueva += random.choice(self.letrasMinus)
                    i += 1
                    
                else:
                    contraseñaNueva += random.choice(self.numeros)
                    i += 1
            
            
        elif especiales == True and mayusculas == False:
            i = 0
            while i < longitud:
                
                x =  random.randint(1,3)
                
                if x == 1:
                    contraseñaNueva += random.choice(self.letrasMinus)
                    i += 1
                    
                elif x == 2:
                    contraseñaNueva += random.choice(self.numeros)
                    i += 1
                    
                else:
                    contraseñaNueva += random.choice(self.caracteresEspeciales)
                    i+= 1
            
            
        elif especiales == False and mayusculas == True:
            i = 0
            while i < longitud:
                
                x =  random.randint(1,3)
                
                if x == 1:
                    contraseñaNueva += random.choice(self.letrasMinus)
                    i += 1
                    
                elif x == 2:
                    contraseñaNueva += random.choice(self.numeros)
                    i += 1
                    
                else:
                    contraseñaNueva += random.choice(self.letrasMayus)
                    i += 1
            
            
        elif especiales == True and mayusculas == True:
            i = 0
            while i < longitud:
                
                x =  random.randint(1,4)
                
                if x == 1:
                    contraseñaNueva += random.choice(self.letrasMinus)
                    i += 1
                    
                elif x == 2:
                    contraseñaNueva += random.choice(self.numeros)
                    i += 1
                    
                elif x == 3:
                    contraseñaNueva += random.choice(self.letrasMayus)
                    i += 1
                    
                else:
                    contraseñaNueva += random.choice(self.caracteresEspeciales)
                    i += 1
        
        return contraseñaNueva
    
    def verificarContraseña(self,contraseña):
        
        numE = 0
        numM = 0
        
        for caracter in contraseña:
            if caracter in self.caracteresEspeciales:
                numE += 1
                
            elif caracter in self.letrasMayus:
                numM += 1
        
        
        if len(contraseña) >= 8 and (numE <= (len(contraseña)/10) and numM <= (len(contraseña)/10)):
            return 2
        
        elif len(contraseña) >= 8 and (numE >= (len(contraseña)/10) and numM <= (len(contraseña)/10)):
            return 3
        
        elif len(contraseña) >= 8 and (numM >= (len(contraseña)/10) and numE <= (len(contraseña)/10)):
            return 3
        
        elif len(contraseña) >= 8 and (numE >= (len(contraseña)/10) and numM >= (len(contraseña)/10)):
            return 4
        
        else:
            return 1