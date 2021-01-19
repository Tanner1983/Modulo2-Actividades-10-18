opcion="";tramo_uno=0;tramo_dos=0;tramo_tres=0;monto_tramo1=0;monto_tramo2=0;monto_tramo3=0
ventas=[]
while opcion !="0":
    respuesta="S"
    print("[1] Ingreso de ventas\n[2] Reporte\n[3] Listar ventas\n[0] Salida")
    opcion=input("Ingrese la opción: ")
    if opcion =="1":
        while respuesta.upper() =="SI" or respuesta.upper() =="S":
            monto_venta=int(input("Ingrese el monto de la venta: $"))
            if monto_venta > 0:                
                if monto_venta <= 10000:
                    tramo_uno+=1
                    monto_tramo1+=monto_venta
                elif monto_venta >10000 and monto_venta <=50000:
                    tramo_dos+=1
                    monto_tramo2+=monto_venta
                else:
                    tramo_tres+=1
                    monto_tramo3+=monto_venta
                ventas.append(monto_venta)
            else:
                print("monto incorrecto")
                input("Presione cualquier tecla para continuar.....\n")
            respuesta=input("Desea ingresar otra venta [SI] o [NO]: ")
    elif opcion =="2":
        print("+-+-+-+-+-+ Reporte de ventas +-+-+-+-+-+\n")
        print(f"Ventas inferiores a $10.000     --- Cantidad {tramo_uno}  ventas --- Monto total: ${monto_tramo1}")
        print(f"Ventas de $10.001 hasta $50.000 --- Cantidad {tramo_dos}  ventas --- Monto total: ${monto_tramo2}")
        print(f"Ventas Superiores a $50.001     --- Cantidad {tramo_tres} ventas  --- Monto total: ${monto_tramo3}")
        
        print("-------\nCantidad total: ",tramo_uno+tramo_dos+tramo_tres)
        print("-------\nTotal de ventas: $", monto_tramo1+monto_tramo2+monto_tramo3)
    elif opcion =="3":
        print("Listado de ventas\n")
        for indice in range(len(ventas)):
            print("Venta n°",indice+1," $",ventas[indice])
    elif opcion =="" or opcion.isalpha()==True or int(opcion) < 0 or int(opcion) >= 3:
        print("Opcion elegida no es valida")
        input("Presione cualquier tecla para continuar.....\n")
    else:
        print("Hasta Pronto!!!")