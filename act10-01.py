boleta=0;inferiores=0;superiores=0;contador=0;cantidad_ventas=0;boletas=0;facturas=0;total=0

print("Ingrese cantidad de ventas que digitara")
ventas=int(input(": "))

while contador < ventas:
    print("Bienvenido: ")
    tipo_venta=input("Que tipo de venta ingresará? [1] Boleta o [2] Factura: ")
    valor_venta=int(input("Ingrese valor de la venta: $"))
    if tipo_venta=="1":
        boletas+=1
    elif tipo_venta=="2":
        facturas+=1
    else:
        print("Tipo de venta incorrecto")
        continue
    if valor_venta <10000:
        inferiores+=valor_venta
    elif valor_venta >150000:
        superiores+=valor_venta
    total+=valor_venta
    contador+=1
    
    print("Cantidad de Ventas:",boletas+facturas)
    print("Cantidad de Boletas: ",boletas)
    print("Cantidad de facturas:",facturas)
    print("Ventas inferiores: $",inferiores)
    print("Ventas Superiores: $",superiores)
    print("Total de ventas: $",total)
    
    salir=input("[1] Salir o presione enter para continuar")
    if salir=="1":
        break