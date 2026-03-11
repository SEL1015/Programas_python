# p085-rombo-caracter
"""
Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo. El pro-
grama deberá dibujar el rombo utilizando el carácter que el usuario elija.
"""
print("\033[H\033[J")
print("---- PROGRAMA PARA DIBUJAR UN ROMBO ----")
n = int(input("Ingrese un número entero impar: "))
caracter = input("Ingrese el carácter para dibujar el rombo: ")

if n % 2 == 0:
    print("El número debe ser impar")
else:
    mtd = n // 2

    # Parte superior
    for i in range(mtd + 1):

        for j in range(mtd - i):
            print(" ", end="")

        for j in range(2*i + 1):
            print(caracter, end="")

        print()

    # Parte inferior
    for i in range(mtd - 1, -1, -1):

        for j in range(mtd - i):
            print(" ", end="")

        for j in range(2*i + 1):
            print(caracter, end="")

        print()#dejar una línea en blanco en la pantalla.
            
            