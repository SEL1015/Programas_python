# p068-conteo-ascendente-for-v2.py
# Imprime los números de 1 a n, en incrementos de m, usando un ciclo for
print("\033[H\033[J")
print(" Iniciando secuencia de conteo ascendente...")
print(" Imprime numeros de 1 a n con ciclo for : \n...")

p = int(input("Desde donde ? "))
n = int(input("Hasta donde  ? "))
i=int(input(" incremento "))
for h in range(1, n+1, i):
    print(h, end=' ')