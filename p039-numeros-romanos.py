#p039-numeros-romanos.py
#Problema: Escribe un programa que pida al usuario un número entero entre 1 y 10 y muestre su equivalente en números romanos. Si el número está fuera de este rango, debe mostrar un mensaje de error.
#Ejemplo de ejecución:
# Entrada: 4
# Salida: IV
# Entrada: 11
# Salida: Error: Número inválido.

print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")

#Entrada de datos

print("Ingresa un numero del 1 al 10 ")

#Declaracion de variables 
numromano = int(input())#convertir a entero  
#Evaluar con sentencias 

if numromano == 1:
    print("I")
elif numromano== 2:
    print("II")
elif numromano == 3:
    print(" II")
elif numromano==4:
    print("IV")
elif numromano ==5:
    print("V ")
elif numromano == 6:
    print("VI")
elif numromano == 7 :
    print("VII")
elif numromano == 8 :
    print("VIII")
elif numromano == 9:
    print("IX")
elif numromano == 10:
    print("X")
else:
    print("Error: Día inválido.")
print("Fin del programa.")
