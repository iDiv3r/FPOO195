
# Ejercicio 3 -----------------------------------------------------------

edad = int(input("Escribe tu edad \n"))

if edad < 4:
    print("Su entrada es gratis")
    
elif edad < 18 and edad >= 4:
    print("Por favor pagar $110")

elif edad >= 18:
    print("Por favor pagar $190")
