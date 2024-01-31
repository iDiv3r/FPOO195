saldo = 0

while True:
    
    respuesta = int(input("Escoge una operación \n 1-Depositar 100 pesos \n 2-Retirar 50 pesos \n 3-Salir \n"))
    

    if respuesta == 1:
        saldo += 100
        print("Se han depositado 100 pesos")
        
    elif respuesta == 2:
        saldo -= 50
        print("Se han retirado 50 ")
            
    elif respuesta != 2 or respuesta != 1:
        print("El saldo restante es:",saldo)
        break
