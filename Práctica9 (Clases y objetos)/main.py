from Personaje import * 
from Arma import *

# Solicitar datos del Spartan
nombreS = input("Escribe el nombre del Spartan: \n")
especieS = input("\n Escribe la especie del Spartan: \n")
alturaS = float(input("\n Escribe la altura del Spartan: \n"))


#Solicitar datos del Némesis
nombreN = input("Escribe el nombre del Némesis: \n")
especieN = input("\n Escribe la especie del Némesis: \n")
alturaN = float(input("\n Escribe la altura del Némesis: \n"))


# Crear instancias del objeto personaje
spartan = Personaje(nombreS, especieS, alturaS)
nemesis = Personaje(nombreN, especieN, alturaN)
arma = Arma()   

# Atributos del Spartan
print("-- El Spartan contiene --")
print(spartan.getNombre())
print(spartan.getEspecie())
print(spartan.getAltura())

# Atributos del Némesis
print("-- El Némesis contiene --")
print(nemesis.getNombre())
print(nemesis.getEspecie())
print(nemesis.getAltura())

# Métodos del Spartan
print("-- Métodos del Spartan --")
spartan.correr(False)
spartan.lanzarGranada()
print("\n")

# Métodos del Némesis
print("-- Métodos del Némesis --")
nemesis.correr(True)
nemesis.lanzarGranada()
print("\n")

# Métodos del arma
arma.seleccionarArma(spartan.getNombre())
arma.recargarArma(50)
