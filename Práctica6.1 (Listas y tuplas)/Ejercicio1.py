import statistics

tupla = tuple(())

while True:
    print("--------------------------------------------------------")
    print("Selecciona una opción \n")
    print("1-Agregar valores a la lista \n")
    print("2-Sumar los elementos de la lista \n")
    print("3-Número mayor de la lista \n")
    print("4-Número menor de la lista \n")
    print("5-Promedio \n")
    print("6-Moda de la lista \n")
    print("7-Rango \n")
    print("8-Mostrar lista")
    
    lista = list(tupla)
    
    opcion = int(input())
    
    long = len(lista)
    
    listaOrd = sorted(lista)
    
    match opcion:
        
        case 1:
            
            numero = int(input("Escribe el número \n"))
            lista.append(numero)
            
            tupla = tuple((lista))
        
        case 2:
            
            total = 0
            i = 0
            while i < long:
                total += lista[i]
                i += 1
            
            print("La suma de todos los números de la lista es:", total, "\n")
            tupla = tuple((lista))
            
        case 3:
            
            print("El número mayor de la lista es:", listaOrd[long-1], "\n")
            tupla = tuple((lista))
            
        case 4:

            print("El número menor de la lista es:", listaOrd[0], "\n")
            tupla = tuple((lista))
            
        case 5:
            
            total = 0
            i = 0
            while i < long:
                total += lista[i]
                i += 1
            
            promedio = (total / long)
            
            print("El promedio de la lista es:", promedio, "\n")
            tupla = tuple((lista))
            
        case 6:
            
            moda = statistics.mode(lista)
            
            print("La moda de la lista es:", moda , "\n")
            tupla = tuple((lista))
            
        case 7:
            
            rango = listaOrd[long-1] - listaOrd[0]
            
            print("El rango de la lista es:", rango, "\n")
            tupla = tuple((lista))
            
        case 8:
            
            print("La lista es:", tupla)