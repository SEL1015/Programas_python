# p069-conteo-descendente-forv2.py
# Imprime los números de 100 a 1 usando un ciclo for
print("\033[H\033[J")
print(" Imprime los numeros del 100 al n en decremento m , con for :\n ...")


n = int(input("Desde donde ? "))
m = int(input("Hasta donde  ? "))
d=int(input(" incremento "))


for x in range(n,m-1,-d):
    print(x,end=' ')