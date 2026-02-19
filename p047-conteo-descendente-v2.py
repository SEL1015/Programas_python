# p047-conteo-descendente-v2.py
# Imprime los números de n a 1, en decrementos de m, usando un ciclo while

print(" Numeros de n a 1 con while ")




n= int(input("Desde donde ?"))
m = int(input("En decremento de ? "))
r = n

while r >= 1:
    print(r)
    r = r - 1

print(f"Ciclo Terminado {r}")