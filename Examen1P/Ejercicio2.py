numero = int(input("Escribe un múltiplo de 10 entre 1 y 1000 \n"))

if numero > 1000:
    print("El número debe ser menor a 1000")
    
elif numero < 1:
    print("El número debe ser mayor a 1")
    

else:
    if numero % 2 != 0:
        print("El número debe ser múltiplo de 10")
    
    else:

        print("Los múltiplos de 10 de", numero,"a 1000 son \n")

        while numero <= 1000:

            print(numero, end=",")
            numero += 10
            
            
