def contRepeticiones(lista):
    
    repeticiones = []
    i = 0
    
    while i < len(lista):
        
        contador = 0
        j = 0 
        while j < len(lista):
            
            if lista[j] == lista [i]:
                contador += 1
            
            j += 1
        
        repeticiones.append(contador)
        i += 1
    
    return repeticiones


def eliminarRepetidos(lista):
    
    lista2 = []

    for numero in lista:
        if numero not in lista2:
            lista2.append(numero)
            
    
    return lista2

def reemplazarACero(lista):
    lista2 = []

    for numero in lista:
        if numero not in lista2:
            lista2.append(numero)
        else:
            lista2.append(0)
            
    
    return lista2
#---------------------------------------------------------

import random

lista = []

i = 0
while i < 30:
    lista.append(random.randrange(10,20))
    i += 1
    

numRep = (contRepeticiones(lista))

while True:
    print("Selecciona una opcion \n")
    print("1-Contar numeros repetidos")
    print("2-Eliminar repetidos")
    print("3-Reemplazar repetidos con 0")
    opcion = int(input())
    
    match opcion:
        case 1:
            k = 10
            while k < 20:

                l = 0
                while l < len(lista):
                    
                    if lista[l] == k:
                        print("El número", k, "aparece", numRep[l], "veces")
                        break
                    
                    l += 1
                
                k += 1
                
        
        case 2:
            
            lista2 = eliminarRepetidos(lista)
            print("La nueva lista sin valores repetidos es:", lista2)
            
        case 3:
            
            print("La lista con valores repetidos a 0 es:", reemplazarACero(lista))










# m = 1
# while m < 10:

#     n = 0
#     while n < len(lista):
        
#         if numRep[n] > 1 and lista[n] == m:
            
#             del lista[n]
#             print(lista)
            
#             n = 0
        
#         n += 1
    
#     m += 1
    
