# p049-sumar-consecutivos.py
# Suma números hasta que el total 5000 pero cuenta hasta 200

print("Cuantos boletis tengo que hacer para juntar 5000")
n=int(input("Cuanto quieres recabar"))
b = 0
d = 0

# El ciclo está programado para correr hasta 200, pero el 'break' lo detendrá antes.
while b < 200:
    b = b +  1
    d = d + b
    print(b, end=" ")


    if d >= n:
        print("\n\n ¡Ya tengo el dinero que me propuse!")
        break
if d < n:
    print("No se alcanzo ")
else:
    print(f" use {b} boletos para llegar a {d}")


