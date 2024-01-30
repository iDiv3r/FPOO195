palabra = input("Ingresa una palabra \n")

contadorVocales = 0 
for letra in palabra:
    if letra.lower() in "aeiou":
        contadorVocales += 1
        
print("La palabra", palabra, "tiene", contadorVocales, "Vocales")