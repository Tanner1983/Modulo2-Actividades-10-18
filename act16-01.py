opcion="";resultado=0

def sumar(num1,num2):
    return int(num1) + int(num2)

def restar(num1,num2):
    return int(num1) - int(num2)

def multiplicar(num1,num2):
    return int(num1) * int(num2)

def dividir(num1,num2):
    return int(num1) / int(num2)

def factorial(numero):
    numero=int(numero)
    factorial_total = 1
    while numero > 1:
        factorial_total *= numero
        numero -= 1
    return factorial_total

def sumatoria(numero):
    numero=int(numero)
    sumatoria_total = 1
    while numero > 1:
        sumatoria_total += numero
        numero -= 1
    return sumatoria_total

while opcion !="0":
    respuesta="S"
    print("[1] Sumar\n[2] Restar\n[3] Multiplicar\n[4] Dividir\n[5] Factorial\n[6] Sumatoria\n[0] Salida")
    opcion=input("Ingrese la opción: ")
    if int(opcion)>=1 and  int(opcion) <=4:
        print("Ingrese dos numeros: ")
        numero1=input(": ")
        numero2=input(": ")
        if opcion=="1":
            resultado=sumar(numero1,numero2)
        elif opcion=="2":
            resultado=restar(numero1,numero2)
        elif opcion=="3":
            resultado=multiplicar(numero1,numero2)
        else:
            if int(numero1)<=0 or int(numero2) <=0:
                print("No es posible llevar a cabo la operacion")
                input("")
            else:
                resultado=dividir(numero1,numero2)
    elif opcion=="5":
        print("Ingrese numero para buscar el factorial: ")
        numero=input(": ")
        resultado=factorial(numero)
    elif opcion=="6":
        print("Ingrese numero para buscar la sumatoria: ")
        numero=input(": ")
        resultado=sumatoria(numero)
    elif opcion =="" or opcion.isalpha()==True or int(opcion) < 0 or int(opcion) >= 3:
        print("Opcion elegida no es valida")
        input("Presione cualquier tecla para continuar.....\n")
    else:
        print("Hasta Pronto!!!")

    print(resultado)