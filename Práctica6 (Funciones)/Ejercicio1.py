def calcularFactura(precio, iva = 0.21):
    
    totIva = iva*precio
    
    factura = totIva + precio
    
    return factura

precio1 = float(input("Escribe el precio que pagaste sin iva \n"))
iva = (input("Escribe el iva en decimal \n"))

if iva != '':
    print("El precio total a pagar es", calcularFactura(precio1, float(iva)))
else:
    print("El precio total a pagar es", calcularFactura(precio1)) 

