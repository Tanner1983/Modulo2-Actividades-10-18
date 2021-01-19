
opcion="";
nombres=[]
while opcion !="0":
    respuesta="S"
    print("[1] Agrege persona\n[2] Ver Nombre\n[0] Salir")
    opcion=input("Ingrese la opción: ")
    if opcion=="1":
        while respuesta.upper() =="SI" or respuesta.upper() =="S":
            ingreso=input("Ingrese nombre de la persona: ")
            nombres.append(ingreso)
            respuesta=input("Desea ingresar otro nombre [SI] o [NO]: ")
            
    elif opcion =="2":
        for nombre in nombres:
            print("* ",nombre)
    elif opcion =="" or opcion.isalpha()==True or int(opcion) < 0 or int(opcion) >= 3:
        print("Opcion elegida no es valida")
        input("Presione cualquier tecla para continuar.....\n")
    else:
        print("Hasta Pronto!!!")
            
        
