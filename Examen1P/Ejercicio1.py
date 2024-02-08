numero = int(input("Escribe un número par entre 200 y 400 \n"))

if numero > 400:
    print("El número debe ser menor a 400")
    
elif numero < 200:
    print("El número debe ser mayor a 200")
    

else:
    if numero % 2 == 1:
        print("El número debe ser par")
    
    else:
        print("Los número entre", numero , "y 400 son: \n")
        
        while numero <= 400:
            print(numero,end=",")
            numero += 2