import os

opcion="";pago_mensual=0;descuento_plan=0;monto=0

planes={"Gold":"4500", "Silver":"3000", "Cooper":"1000"} # Definicion de planes en diccionario

totales=[] #Lista con los montos de ventas

set_rut=set() #Conjunto con los rut ingresados

def menuPrincipal(): #Menu principal
    os.system("cls")
    print("=== BIENVENIDO A SPOTYSOUNDMASTER ====\n")
    print("[1] Contratar Plan\n[2] Cierre de Caja\n[0] Salir")
    return

def menuCierre(): #Submenu del cierre de caja
    os.system("cls")
    print("=== MENÚ CIERRE DE CAJA ====\n")
    print("[1] Total de recaudación\n[2] Listar los montos registrados\n[3] Listar los rut registrados\n[0] Volver")
    return

def printMonto(monto):
    print("\n========================================================\n")
    print("El monto total recaudado en ventas es: $", monto) 
    print("\n==========================================================")                   
    input("")
    return

def printDescuento():
    print("\n=================================================================\n")
    print("¡¡¡ Usuario Registrado se aplicará descuento del 50% en el total !!!")
    print("\n==================================================================") 
    return

def printPlan(tipo_plan,valor,cantidad):    
    print(f"\nInformacion del plan {tipo_plan}, Precio mensual de ${valor}, cantidad solicitada {cantidad}, Total a Pagar: ",int(valor)*int(cantidad))

while opcion !="0":
    submenu="";x=0;plan=0;cantidad=0
    respuesta="S"
    menuPrincipal()
    opcion=input("Ingrese la opción: ")
    if opcion=="1":
        print("=== BIENVENIDO A SPOTYSOUNDMASTER ====\n\nConozca nuestro planes")
        for key,precio in planes.items(): #Cargar el diccionario para mostrar los datos
            x+=1 
            print(f"[{x}] Plan: {key} Precio Mensual: ${precio}")
            
        plan=int(input("\nIngrese el n° Correspondiente al plan que desea contratar... : "))

        while int(plan) < 1 or plan > 3:                                    #Validacion del plan
            print("Opción ingresada es incorrecta...")
            plan=int(input("\nIngrese el n° Correspondiente al plan que desea contratar... : "))            
            
        
        cantidad=int(input("Ingrese cantidad de planes a contratar... : ")) #Ingreso de cantidad de planes 
        while int(cantidad) <=0:                                           #Validacion de la cantidad
            print("Cantidad ingresada es incorrecta...")
            cantidad=int(input("Ingrese cantidad de planes a contratar... : "))    
                      
        if plan==1:            
            tipo_plan="Gold"
            valor=4500
            printPlan(tipo_plan,valor,cantidad)                             # Mensaje con informacion al usuario en funcion
        elif plan==2:
            valor=3000
            tipo_plan="Silver"
            printPlan(tipo_plan,valor,cantidad)
        else:
            valor=1000
            tipo_plan="Cooper"
            printPlan(tipo_plan,valor,cantidad)

        rut=0
        contrata=input("Desea realizar la contratacion del plan... [SI] o [NO]: ")
        if contrata.upper()=="SI" or contrata.upper()=="S":
            while int(rut)<=0:
                rut=input("\nPara realizar la contratacion del o los planes ingrese su rut (SIN DIGITO VERIFICADOR): ") # Ingreso de rut del cliente
                    
            for x in set_rut:                                                                # Ciclo para validar si el rut existe
                if x==rut:
                    descuento_plan=(valor*cantidad)*0.5
                    printDescuento()
                                
            pago_mensual=(valor*cantidad)-descuento_plan
            set_rut.add(rut)
            totales.append(pago_mensual)
            print(f"\nLa contratacion se ha realizado exitosamente\n\nPlan Contratado {tipo_plan}\nValor Mensual ${valor}\nCantidad de planes: {cantidad}\nTOTAL MENSUAL A PAGAR: {pago_mensual}")
            input("")
        else:
            input("Presione tecla para volver al menú principal......")
        
    if opcion =="2":
        while submenu !="0":
            menuCierre()
            submenu=input("Ingrese la opción: ")
            if submenu=="1":
                monto=0
                print("\nTotal de ventas por concepto de venta de Planes")
                for total in totales: #Recorre la lista totales y entrega el total
                    monto+=int(total)
                printMonto(monto)
                menuCierre()
            elif submenu=="2":
                x=0
                print("\nMontos registrados por concepto de venta de Planes\n**************************************************")
                for total in totales: #Recorre y muestra todas las ventas guardadas en totales
                    x+=1
                    print(f"{x}° Venta por un monto de $",total)
                print("**************************************************")    
                input("")
                menuCierre()    
            elif submenu=="3": #Recorre el set con los rut registrados
                x=0
                print("\nUsuarios que han sido Registrados\n**************************************************")
                for x in set_rut:
                    print("→ → RUT:  ", x)    
                input("")
                menuCierre()        
            elif submenu =="" or submenu.isalpha()==True or int(submenu) < 0 or int(submenu) >= 3:
                print("Opcion elegida no es valida")
                input("Presione cualquier tecla para continuar.....\n")
            else:
                menuPrincipal()

    elif opcion =="" or opcion.isalpha()==True or int(opcion) < 0 or int(opcion) >= 3:
        print("Opcion elegida no es valida")
        input("Presione cualquier tecla para continuar.....\n")
    else:
        print("Hasta Pronto!!!")
        print("GRACIAS POR PREFERIR SPOTYSOUNDMASTER")

