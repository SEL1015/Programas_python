# p044-conteo-ascendente.py
# Imprime los números de 1 a 100 usando un ciclo while

print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")
print(" Iniciando secuencia de conteo ascendente...")

z = 1
while z <= 100:
    print(z, end='')
    z= z+1

    print(f"\n ¡Ciclo terminado {z}!")
