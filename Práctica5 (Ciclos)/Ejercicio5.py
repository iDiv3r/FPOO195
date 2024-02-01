frase = str(input("Escribe una frase \n"))
letraU = str(input("Escribe una letra \n"))

contLetras = 0

for letra in frase:
    if letra.lower() in letraU:
        contLetras += 1
        

print("La letra", letraU, "aparece", contLetras, "veces en la frase", frase)