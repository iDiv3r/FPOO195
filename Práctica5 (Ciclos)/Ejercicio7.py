numero = int(input("Escribe un número entero positivo \n"))

numero2 = numero

i = 1

while i <= numero:
    numEstrellas = ((i*2)-1)
    espacios = numero2
    
    j = 0
    
    while j <= (numero*2+2):
        
        if espacios > 0:
            print(end= " ")
        elif numEstrellas > 0:
            print(end = "*")
            numEstrellas -= 1
        
        espacios -= 1
        j += 1
        
    
    print("\n")
    numero2 -= 1
    i += 1