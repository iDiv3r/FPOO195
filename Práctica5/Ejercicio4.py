numero = int(input("Escribe un numero impar \n"))

contador = 0

i = 1


while i <= numero:
    contador = i
    j = 1
    
    while j <= numero:
        if contador > 0:
            print(contador, end = " ")
        
        contador -= 2
        j += 2
    
    print("\n")
    i += 2       