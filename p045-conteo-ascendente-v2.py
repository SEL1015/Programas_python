# p045-conteo-ascendente-v2.py
# Imprime los números de 1 a n, en incrementos de m, usando un ciclo while
print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")



print(" Iniciando secuencia de conteo ascendente...")
n = int(input("Hasta donde ? "))#FIN DEL CICLO 
m = int(input("De cuanto en cuanto ? "))#INCREMENTO 

z = 0
while z <= n:
    print(z, end="")
    z = z + m
    print(F"\n ¡Secuencia completada!{z}")