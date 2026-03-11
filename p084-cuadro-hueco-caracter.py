#p084-cuadro-hueco-caracter
"""
El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se
dibujará. Luego, deberá imprimir en la consola un "cuadrado hueco", donde el carácter solo se utilice para dibujar
el contorno del mismo.
"""
# Imprime el tamaño del cuadrado 
print('\033[H\033[J')
lado = int(input("¿Cuántos renglones tendrá cuadrado ? "))
car = input("¿Qué carácter quieres usar para dibujar? ")

print("\n--- Cuadrado  Generado ---")
# Bucle exterior: controla las filas
for i in range(lado):
    for j in range(lado):

        if i == 0 or i == lado-1 or j == 0 or j == lado-1:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()#dejar una línea en blanco en la pantalla.