
# Ejercicio 3 -----------------------------------------------------------

texto = str(input("Escriba una palabra \n"))

textoInv = texto[::-1]

if texto == textoInv:
    print("La palabra", texto, "es una palabra paíndroma")
    
else:
    print("La palabra", texto, "no es una palabra palíndroma")