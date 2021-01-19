opcion="";a="";x=0
productos={}

while opcion !="0":
    respuesta="S"
    print("[1] Ingresar Producto\n[2] Eliminar Producto\n[3] Modificar Producto\n[4] Listar Productos\n[5] Venta Producto\n[0] Salida")
    opcion=input("Ingrese la opción: ")

    if opcion=="1":
        while respuesta.upper() =="SI" or respuesta.upper() =="S":
            print("ingrese el codigo producto ")
            codigo=input(": ")
            print("ingrese precio producto")
            precio=input(": ")
            productos[codigo]=precio
            input("Producto Agregado.....")
            respuesta = input("\nDesea ingresar otro producto: [S] ")
    elif opcion=="2":        
        print("ingrese el codigo que desea eliminar")
        eliminar=input(": ")
        pregunta=input("Esta seguro que desea eliminar? [SI] o [NO]")
        if pregunta.upper()=="S" or pregunta.upper()=="SI":
            productos.pop(eliminar)
            print("El producto fue Eliminado")
    elif opcion=="3":
        print("Ingrese el codigo que desea Modificar...")
        buscar=input(": ")
        for key,precio in productos.items():
            if buscar==key:
                nuevo_precio=input("ingrese nuevo precio: $")
                productos[key]=nuevo_precio
                a="Modificado"
        if a=="Modificado":
            print(f"El producto fue {a}")
            input("")
        else:
            print("No se encontro el codigo")
            input("")
    elif opcion =="4":
        print("========================================")
        for key,precio in productos.items():
            print(f"Producto: {key} Precio: ${precio}")
        print("========================================")
        input("")
    elif opcion=="5":
        venta=input("Ingrese codigo a comprar: ")
        for key,precio in productos.items():
            if venta==key:
                print("========================================")
                print(f"Producto: {key} Precio: ${precio}")
                print("Gracias por su compra =)")
                input("")
                print("\n========================================")
                x=1
        if x==0:
            print("Producto no encontrado....")
            input("")
    elif opcion =="" or opcion.isalpha()==True or int(opcion) < 0 or int(opcion) >= 3:
        print("Opcion elegida no es valida")
        input("Presione cualquier tecla para continuar.....\n")
    else:
        print("Hasta Pronto!!!")
        
