#p086-triangulo-invertido-numeros
"""
Solicitar al usuario un número entero n que determinará la altura de un triángulo numérico invertido. El programa
debe imprimir n renglones. El primer renglón contendrá los números de 1 a n, el segundo de 1 a n-1, y así sucesi-
vamente hasta que el último renglón contenga solo el número 1.
"""
print("\033[H\033[J")

print("TRIÁNGULO NUMÉRICO INVERTIDO")

n = int(input("Ingrese un número entero: "))

if n > 0:

    for i in range(n, 0, -1):      # controla los renglones
        for j in range(1, i + 1):  # imprime los números
            print(j, end=" ")
        print()

else:
    print("El número debe ser mayor que 0")