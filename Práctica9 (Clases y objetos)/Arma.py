class Arma:
    
    def seleccionarArma(self, nombre):
        seleccion = int(input("Selecciona el arma: \n 1- Rifle de asalto \n 2- Espada de energia \n 3- Rifle M392 \n"))
        
        match seleccion:
            case 1:
                print("Rifle de asalto asignado a", nombre)
                print("Municiones 7.62 * 52mm, sin mira")
                
            case 2:
                print("Espada de energía asignada a", nombre)
                print("Arma creada por los Shagheili")
                
            case 3: 
                print("Rifle M392 asignado a", nombre)
                print("Municiones 7.62 * 52mm, con mira")
                
            case _:
                print("error")
                
        
    def recargarArma(self, municion):
        cargador = 25
        cargador  += municion
        print("Arma recargada al", str(cargador), "%")
        
    