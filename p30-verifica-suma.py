# p30-verifica-suma.py
# Verificar si la suma de dos números es igual a un tercero.
# n1 n2 n3   n1 n2 n3 n1 n2 n3  n1 n2 n3  n1 n2 n3 
# 5 4 = 9    10 20 10 5 3 2 10 10 10       1 5 7 
print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")
#Muestra el mensaje principal 
print("Verificar si la suma de dos números es igual a un tercero ")

print("Dame 3 números enteros separados por espacio:")
#Declarar variables 
n1, n2, n3 = input().split()# .split es separa por un espacio oh coma 

# Asignar y convertir las entradas a enteros
n1, n2, n3 = int(n1), int(n2), int(n3)

# Evaluar las posibles combinaciones con if/elif
if n1 + n2 == n3:

    print(f"n1 + n2 es igual a n3 ({n1} + {n2} = {n3})")##impirme el resultado de la combinacion de suma 

elif n1 + n3 == n2:

    print(f"n1 + n3 es igual a n2 ({n1} + {n3} = {n2})")

elif n2 + n3 == n1:

    print(f"n2 + n3 es igual a n1 ({n2} + {n3} = {n1})")
elif n2== n3== n1:
    print(f"Fue igual a {n1}= {n2} ={n3}")

else:
# Si ninguna de las condiciones anteriores se cumple
    print(f"Todos los numeros son diferentes : {n1} , {n2}, {n3}")


print("\n Gracias por utilizar este Programa ")
