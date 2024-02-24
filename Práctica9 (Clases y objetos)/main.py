from Personaje import * 
from Arma import *

# Crear instancias del objeto personaje

spartan = Personaje()
arma = Arma()   

# Atributos del Spartan

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)


# Métodos del Spartan

spartan.correr(True)
spartan.lanzarGranada()


# Métodos del arma

arma.seleccionarArma(spartan.nombre)
arma.recargarArma(50)
