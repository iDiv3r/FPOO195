import math

def calcularÁreaCirculo(radio):
    area = (math.pi* (radio*radio))
    return area

def calcularVolumenCilindro(radio, altura):
    volumen = calcularÁreaCirculo(radio) * altura
    return volumen

radio = float(input("Escribe el radio del cilindro \n"))
altura = float(input("Escribe la altura del cilindro \n"))

print("El área de un círculo de radio", radio, "es", calcularÁreaCirculo(radio), "y su cilindro es",calcularVolumenCilindro(radio, altura))

