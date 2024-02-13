import random

lista = list(30)

i = 0
while i < 30:
    lista[i] = random.randrange(10,20)
    i += 1
    

print(lista)