import os
opcion=""
plan1="";plan2="";plan3=""
valor_plan=0;total=0; valor_plan1=0; valor_plan2=0; valor_plan3=0;contratados=0;uno=0;dos=0;tres=0


def menuPrincipal():
    os.system('cls')
    
    print("=*=*=*=*=*=*=* Menu inicial =*=*=*=*=*=*=*\n")
    print("Seleccione una opción")
    print("[1] - Ingresar precios de los planes")
    print("[2] - Realizar la contratación del plan")
    print("[3] - Cierre de turno")
    print("[4] - Salir")
    return


def menuPlan(plan1,plan2,plan3):
    os.system('cls')
    
    print("=*=*=*=*=*=*=* Bienvenido a Nesfli =*=*=*=*=*=*=*\n")
    print("Seleccione su plan a contratar")
    print(f"[1] - Plan 2 pantallas ${plan1}")
    print(f"[2] - Plan 5 pantallas Full HD ${plan2}")
    print(f"[3] - Plan Ilimitado ${plan3}")
    print("[4] - Volver")
    return    
    
    
def menuCierre():
    os.system('cls')
    
    print("=*=*=*=*=*=*=* Menu de Cierre =*=*=*=*=*=*=*\n")
    print("Al realizar el cierre se vuelven a 0 los valores")
    print("Seleccione una opcion")
    print(f"[1] - Total de recaudacion")
    print(f"[2] - Cantidad de planes vendidos")    
    return

while True:
    menuPrincipal()    
    opcion = input("Ingrese el numero correspondiente a la opcion que desea >>>> ")

    if opcion == "1":
        os.system('cls')
        
        print("\n=*=*=*=*=*=*=* Configuración de valores =*=*=*=*=*=*=*\nAsigne los valores correspondientes a los planes\n")
        plan1=input("Plan 2 pantallas HD: ")
        while int(plan1)<=0:
            input("Valor ingresado es incorrecto, ingrese valor nuevamente\nPresione Enter..")
            plan1=input("Plan 2 pantallas HD: ")
        plan2 = input("\nPlan 5 pantallas Full HD: ")
        while int(plan2)<=0:
            input("Valor ingresado es incorrecto, ingrese valor nuevamente\nPresione Enter..")
            plan2 = input("\nPlan 5 pantallas Full HD: ")
        plan3 = input("\nPlan Ilimitado: ")
        while int(plan3)<=0:
            input("Valor ingresado es incorrecto, ingrese valor nuevamente\nPresione Enter..")
            plan3 = input("\nPlan Ilimitado: ")
        print("===============================")
        print(f"Planes Registrados correctamente\nPlan 2 pantallas HD ${plan1}\nPlan 5 pantallas Full HD ${plan2}\nPlan Ilimitado ${plan3}\n===============================")
        print("")
        input("Presione una tecla para continuar....")
        
    elif opcion=="2":
        if plan1 == "" or plan2 =="" or plan3 =="":
            input("No estan ingresados los valores de los planes\nSeleccione opcion 1 en menú\nPresione Enter.....")
        else:  
            menuPlan(plan1,plan2,plan3)
            plan=input("Ingrese el numero correspondiente al plan >>>> ")
            
            if plan=="1":
                cantidad_planes=int(input("¿Cuantos planes contratará?: "))
                while cantidad_planes<=0:
                    input("Cantidad ingresada es invalida")
                    cantidad_planes=int(input("¿Cuantos planes contratará?: "))
                
                print(f"Usted va a contratar {cantidad_planes} del plan n°2 con valor {plan1} mensual\nTotal a Pagar mensualmente: $",int(plan1)*cantidad_planes)
                respuesta=input("\nDesea realizar el pago y la contratacion del servicio? [SI] o [NO]: ")
                
                if respuesta.upper()== "SI" or respuesta.upper() == "S":
                    pago=int(input("Ingrese cantidad con la que pagará: "))
                    while pago <=0 or pago < int(plan1)*cantidad_planes:
                        input("Valor ingresado es incorrecto, ingrese valor nuevamente\nPresione Enter..")
                        pago=int(input("Ingrese cantidad con la que pagará: "))

                    print("el vuelto a entregar al cliente es: $",pago-int(plan1)*cantidad_planes)    
                    valor_plan1+=int(plan1)*cantidad_planes
                    contratados+=cantidad_planes
                    uno+=cantidad_planes
                    print(f"Plan Contratado n°1 con valor {plan1} mensual\nTotal a Pagar mensualmente: $",int(plan1)*cantidad_planes)
                    input("\nPresione una tecla para continuar....")
                else:
                    input("Contratacion cancelada")
                
            elif plan=="2":
                cantidad_planes=int(input("¿Cuantos planes contratará?: "))
                while cantidad_planes<=0:
                    input("Cantidad ingresada es invalida")
                    cantidad_planes=int(input("¿Cuantos planes contratará?: "))
                
                print(f"Usted va a contratar {cantidad_planes} del plan n°2 con valor {plan1} mensual\nTotal a Pagar mensualmente: $",int(plan2)*cantidad_planes)
                respuesta=input("\nDesea realizar el pago y la contratacion del servicio? [SI] o [NO]: ")
                
                if respuesta.upper()== "SI" or respuesta.upper() == "S":
                    pago=int(input("Ingrese cantidad con la que pagará: "))
                    while pago <=0 or pago < int(plan2)*cantidad_planes:
                        input("Valor ingresado es incorrecto, ingrese valor nuevamente\nPresione Enter..")
                        pago=int(input("Ingrese cantidad con la que pagará: "))

                    print("el vuelto a entregar al cliente es: $",pago-int(plan2)*cantidad_planes)    
                    valor_plan2+=int(plan2)*cantidad_planes
                    contratados+=cantidad_planes
                    dos+=cantidad_planes
                    print(f"Plan Contratado n°2 con valor {plan2} mensual\nTotal a Pagar mensualmente: $",int(plan2)*cantidad_planes)
                    input("\nPresione una tecla para continuar....")
                else:
                    input("Contratacion cancelada")     
                
            elif plan=="3":
                cantidad_planes=int(input("¿Cuantos planes contratará?: "))
                while cantidad_planes<=0:
                    input("Cantidad ingresada es invalida")
                    cantidad_planes=int(input("¿Cuantos planes contratará?: "))
                
                print(f"Usted va a contratar {cantidad_planes} del plan n°2 con valor {plan3} mensual\nTotal a Pagar mensualmente: $",int(plan3)*cantidad_planes)
                respuesta=input("\nDesea realizar el pago y la contratacion del servicio? [SI] o [NO]: ")
                
                if respuesta.upper()== "SI" or respuesta.upper() == "S":
                    pago=int(input("Ingrese cantidad con la que pagará: "))
                    while pago <=0 or pago < int(plan3)*cantidad_planes:
                        input("Valor ingresado es incorrecto, ingrese valor nuevamente\nPresione Enter..")
                        pago=int(input("Ingrese cantidad con la que pagará: "))

                    print("el vuelto a entregar al cliente es: $",pago-int(plan3)*cantidad_planes)    
                    valor_plan3+=int(plan3)*cantidad_planes
                    contratados+=cantidad_planes
                    tres+=cantidad_planes
                    print(f"Plan Contratado n°3 con valor {plan3} mensual\nTotal a Pagar mensualmente: $",int(plan3)*cantidad_planes)
                    input("\nPresione una tecla para continuar....")
                else:
                    input("Contratacion cancelada")  
                        
            elif int(plan) > 4 or int(plan) < 0:
                print("Ha ingresado una opcion incorrecta")
                input("Presione una tecla para continuar....")
        
    elif opcion=="3":
        if plan1 == "" or plan2 =="" or plan3 =="":
            input("No estan ingresados los valores de los planes\nSeleccione opcion 1 en menú\nPresione Enter.....")
        else:
            os.system('cls')
            menuCierre()
            cierre = input("Ingrese el numero correspondiente a la opcion que desea >>>> ")
            if cierre=="1":
                print("==================== Totales ====================")
                print(f"Plan 2 pantallas -- valor total ${valor_plan1}")
                print(f"Plan 5 pantallas -- valor total ${valor_plan2}")
                print(f"Plan Ilimitado   -- valor total ${valor_plan3}\n")
                print("Las ventas Totales son: ",int(valor_plan1)+int(valor_plan2)+int(valor_plan3))
                print("")
                valor_plan1=0;valor_plan2=0;valor_plan3=0
                input("Presione una tecla para continuar....")
            elif cierre =="2":
                os.system('cls')
                
                print("Total de planes que han sido contratos\n")
                print(f"Plan 2 pantallas -- cantidad vendida {uno} planes")
                print(f"Plan 5 pantallas -- cantidad vendida {dos} planes")
                print(f"Plan Ilimitado   -- cantidad vendida {tres} planes")
                print(f"---------------------------------------------------------\nSe han vendido en total {contratados} planes\n")
                uno=0;dos=0;tres=0;contratados=0
                plan1="";plan2="";plan3=""
                input("Presione una tecla para continuar....")
                  
    elif int(opcion) > 4 or int(opcion) <=0:
       print("Ha ingresado una opcion incorrecta")
       input("Presione una tecla para continuar....")
    else:
        print("Hasta Pronto, gracias por preferir nesfli")
        break
        
    
