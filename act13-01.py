import statistics as stats

numeros=[80, 63, 80, 75, 5, 82, 15, 46, 75, 84, 76, 6, 30, 91, 91, 35, 73, 9, 92, 82, 26, 2, 54, 5, 25, 27, 47, 21, 14, 22, 65, 49, 22, 99, 17, 73, 74, 87, 18, 88, 8, 20, 61, 63, 92, 15, 12, 16, 56, 96, 84, 34, 78, 15, 59, 74, 39, 45, 75, 68, 56, 45, 64, 98, 53, 7, 99, 23, 19, 36, 56, 38, 87, 78, 48, 15, 53, 37, 80, 25, 71, 84, 67, 35, 96, 16, 27, 93, 49, 91, 83, 36, 81, 31, 94, 14, 76, 14, 9, 9]
mayor=0;menor=100;contador_menor=0;contador_mayor=0;indice_mayor=0;indice_menor=0;suma=0
indices_pares=[]

for indice in range(len(numeros)):
    if numeros[indice]>mayor:
        mayor=int(numeros[indice])
        indice_mayor=int(indice)        
        
    if numeros[indice]<menor:
        menor=int(numeros[indice])
        indice_menor=int(indice)

    if indice % 2 == 0:
        indices_pares.append(numeros[indice])
        #print("Numero con indice par: ",indice," ", numeros[indice])

    suma+=numeros[indice]    


for numero in numeros:
    if numero == mayor:
        contador_mayor+=1

    if numero == menor:
        contador_menor+=1
        
        
n = len(numeros)
if n < 1:
    print("No hay") 
if n % 2 == 1:
    mediana =sorted(numeros)[n//2]
else:
    mediana = sum(sorted(numeros)[n//2-1:n//2+1])/2.0


repeticiones = 0
for i in numeros:
    n = numeros.count(i)
    if n > repeticiones:
        repeticiones = n
moda = [] #Arreglo donde se guardara el o los valores de mayor frecuencia 
for i in numeros:
    n = numeros.count(i) # Devuelve el número de veces que x aparece enla lista.
    if n == repeticiones and i not in moda:
        moda.append(i)

if len(moda) != len(numeros):
    moda_final=moda
else:
    print ('No hay moda')
    
frecuencia_Numeros = []
for numero in numeros:
    frecuencia_Numeros.append(numeros.count(numero))

print(frecuencia_Numeros)


frecuencia_Numeros = {}
numeros2=sorted(numeros)
for numero in numeros:
    frecuencia_Numeros[numero]=numeros.count(numero)
    


sumacion=0
promedio=suma/len(numeros)

for numero in numeros:
    resultado = numero-promedio
    elevado=resultado * resultado
    sumacion+=elevado

final=sumacion/len(numeros)

print(f"Numero mayor: {mayor}  Su indice es: {indice_mayor}")
print(f"Numero menor: {menor}   Su indice es: {indice_menor}")

print("Numero mayor se repite: ",contador_mayor)
print("Numero menor se repite: ",contador_menor)

print("\nNumero con indice par: ",indices_pares)
print("\nLa media es: ",suma/len(numeros) )
print("\nLa mediana es: ", mediana )
print("\nLa Moda es: ", moda_final)
print("\nFrecuencia: ",frecuencia_Numeros)
print("\nDesviacion Standard: ",final**0.5)





    
