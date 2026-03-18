#p102-listas-aleatorios-suma.py
"""
Generar 2 listas de 10 números aleatorios cada una. Crear una tercera lista donde el elemento sea la suma de
los correspondientes de las listas A y B, solo si AMBOS elementos son impares; de lo contrario, el elemento de
la tercera lista será 0. Imprimir las 3 listas.
Ejemplo:
--- Listas Generadas ---
Lista A: [15, 8, 3, 12, 1, 7, 2, 9, 10, 5]
Lista B: [4, 1, 9, 6, 3, 11, 14, 2, 17, 1]
--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---
Lista C: [0, 0, 12, 0, 4, 18, 0, 0, 0, 6]
(Ej: A[2]=3, B[2]=9 -> 3+9=12. A[1]=8 (par), B[1]=1 (impar) -> 0)
"""

##DECLARACION DE VARIABLES 


print('\033[H\033[J')
listaA = []
listaB = []
listaC = []

print("Ingrese 10 números para la Lista A:")
for i in range(10):
    num = int(input(f"A[{i}] = "))
    listaA.append(num)

print("\nIngrese 10 números para la Lista B:")
for i in range(10):
    num = int(input(f"B[{i}] = "))
    listaB.append(num)

for i in range(10):
    if listaA[i] % 2 != 0 and listaB[i] % 2 != 0:
        listaC.append(listaA[i] + listaB[i])
    else:
        listaC.append(0)

print("\n--- Listas Generadas ---")
print("Lista A:", listaA)
print("Lista B:", listaB)

print("\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---")
print("Lista C:", listaC)