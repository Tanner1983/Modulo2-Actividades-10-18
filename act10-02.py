opcion = ""
while opcion != 0:
    print("Calculadora")
    print("[1] Sumar")
    print("[2] Restar")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Salir")
    opcion = int(input("Ingrese opcion: "))
    if opcion ==1:
        num1=int(input("Ingrese número: "))
        num2=int(input("Ingrese número: "))
        print("Resultado de la suma", num1+num2)
        input("Presione una tecla para continuar.....")
    elif opcion ==2:
        num1=int(input("Ingrese número: "))
        num2=int(input("Ingrese número: "))
        print("Resultado de la suma", num1-num2)
        input("Presione una tecla para continuar.....")
    elif opcion ==3:
        num1=int(input("Ingrese número: "))
        num2=int(input("Ingrese número: "))
        print("Resultado de la suma", num1*num2)
        input("Presione una tecla para continuar.....")
    elif opcion ==4:
        num1=int(input("Ingrese número: "))        
        num2=int(input("Ingrese número: "))
        if num2 <=0 or num1<=0:
            print("Error en el numero ingresado")
            input("Presione una tecla para continuar.....")
        else:
            print("Resultado de la suma", num1/num2)
    elif opcion ==5:
        break
    else:
        print("Opcion invalida")
        input("Presione una tecla para continuar......")
