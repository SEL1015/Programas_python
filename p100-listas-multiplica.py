# p100-listas-multiplica.py
"""
Leer dos listas, cada una con 5 elementos numéricos. Crear una tercera lista multiplicando los elementos de las
dos listas correspondientes. Imprimir las tres listas.
"""
print('\033[H\033[J')

listaA = []
listaB = []
listaC = []

for i in range(5):
    num = int(input("📋📋📋Introduzca 5 números para la Lista A : 📋📋📋 "))
    listaA.append(num)

for i in range(5):
    num = int(input("📋📋📋Introduzca 5 números para la Lista B :📋📋📋 "))
    listaB.append(num)

for i in range(5):
    listaC.append(listaA[i] * listaB[i])

print("Lista A:", listaA)
print("Lista B:", listaB)
print("Lista C (A*B):", listaC)