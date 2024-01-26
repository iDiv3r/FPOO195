
# Ejercicio 3 -----------------------------------------------------------

numero = int(input("\n Escribe un numero entero \n"))

suma = 0

if numero > 0:
    while numero > 0:
        suma += numero
        numero -= 1

else:
    print("No puedes introducir numeros negativos")
    

print(suma)