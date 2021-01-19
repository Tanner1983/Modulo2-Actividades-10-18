
opcion="";cantidad=0
hinchas=[]
while opcion !="0":
    respuesta="S"
    print("[1] Ingresar hincha\n[2] Ver listado\n[0] Salir")
    opcion=input("Ingrese la opción: ")
    if opcion =="1":
        while respuesta.upper() =="SI" or respuesta.upper() =="S":
            rut=input("Ingrese el rut: ")
            ingreso=input("Permite el ingreso del hincha: [SI] o [NO]")
            if ingreso.upper() =="SI" or ingreso.upper() =="S":
                if rut in hinchas:    
                    print("\n\n*******************\n La persona ya ingreso \n*******************\n") 
                else:
                    cantidad+=1
                    hinchas.append(rut)
                    print("Ingresado")
            else:                
                print("ACCESO DENEGADO!!!")
                input("")
            respuesta=input("\nDesea ingresar otro hincha [SI] o [NO]: ")
    elif opcion =="2":
        print("Listado de hinchas que ingresaron")
        for hincha in hinchas:
            print(hincha)
        input("")
    elif opcion =="" or opcion.isalpha()==True or int(opcion) < 0 or int(opcion) >= 3:
        print("Opcion elegida no es valida")
        input("Presione cualquier tecla para continuar.....\n")
    else:
        print("Hasta Pronto!!!")