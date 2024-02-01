def convertirABinario(decimal):
    binarioInv = ""
    num = int(decimal)
    
    if num != 0:
        while num > 0 :
            residuo = int((num%2))
            binarioInv += str(residuo)
            num = num // 2
        
        binario = binarioInv[::-1]
    else:
        binario = num
        
    return binario

    # return bin(decimal)
    

numero =  int(input("Escribe un numero entero \n"))

print("El número", numero, "en binario es", convertirABinario(numero))