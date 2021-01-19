opcion=""
nombres=["Hugo", "Paco", "Luis"]

def menu():
    print("[1] Ingresar Nombres\n[2] Ver Nombres\n[0] Salir")
    return

def listar_nombre():
    print("======== Listado de Nombres =========")
    for nombre in nombres:
        print("\nNombre: ", nombre)    
    print("======================================")
    input("")

def ingreso(nombre):
    nombres.append(nombre)
    print("Agregado...")
    input("")
    return

def validar_nombre(nombrecillo):
    for nombre in nombres:
        if nombre==nombrecillo:
            print("El nombre ya se encuentra registrado!!\n======")
            input("")
            return    

while opcion !="0":
    respuesta="S"
    menu()
    opcion=input("Ingrese la opción: ")

    if opcion=="1":
        while respuesta.upper()=="S" or respuesta.upper()=="SI":
            nombrecillo=input("Ingrese nombre: ")
            validar_nombre(nombrecillo)
            ingreso(nombrecillo)
            respuesta=input("Desea ingresar otro nombre? [SI]: ")            
        
    elif opcion =="2":
        listar_nombre()
    elif opcion =="" or opcion.isalpha()==True or int(opcion) < 0 or int(opcion) >= 3:
        print("Opcion elegida no es valida")
        input("Presione cualquier tecla para continuar.....\n")
    else:
        print("Hasta Pronto!!!")