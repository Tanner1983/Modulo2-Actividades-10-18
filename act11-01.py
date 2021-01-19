
opcion = "";minutos=0

while opcion != "0":

    print("************ Servicio de estacionamiento ***********")
    print("[1] Ingreso de Minutos")
    print("[2] Total a pagar")
    print("[0] Salir")

    opcion = input("Ingrese su opcion: ")

    if opcion == "1":
       minutos=int(input("Ingrese cantidad de minutos\n: "))
       while minutos <=0:           
           print("cantidad de minutos erronea seleccione opción ")
           input("Presione una tecla para continuar.....")
           minutos=int(input("Ingrese cantidad de minutos\n: "))
    elif opcion=="2":
       if minutos <=0:
           print("cantidad de minutos erronea seleccione opción 1")
           input("Presione una tecla para continuar.....")
       
       elif minutos <=30:
           valor_pagar=600
           print("El valor a pagar es: ", valor_pagar)
           minutos=0
       else:
            valor_pagar=((minutos-30)*25)+600
            print("El valor a pagar es: ", valor_pagar)
            minutos=0
       
    elif opcion == "0":
        break
    else:
        print("Opcion Inválida")
        input("Presione una tecla para continuar.....")
