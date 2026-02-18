#p043-calculadora-anio-bisiesto.py
#Problema: Escribe un programa que determine si un año, ingresado por el usuario, es bisiesto. Un año es bisiesto si cumple una de las siguientes condiciones:
#1. Es divisible por 4, pero no es divisible por 100.
#2. Es divisible por 400.
#El programa debe indicar claramente si el año es bisiesto o no.
#Ejemplos de ejecución:
#• Entrada: 2024
# Salida: El año 2024 es bisiesto. (Porque es divisible por 4 pero no por 100).
#• Entrada: 1900
#• Salida: El año 1900 no es bisiesto. (Porque es divisible por 100 pero no por 400).
#• Entrada: 2000
#• Salida: El año 2000 es bisiesto. (Porque es divisible por 400).
#• Entrada: 2023
#• Salida: El año 2023 no es bisiesto. (Porque no es divisible por 4).

print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]") 

#Entrada de datos
print("PROGRAMA PARA DETERMINAR SI UN AÑO ES BICIESTO  ")

#Declaracion de variables

datos= input("Programa  para saber si es biciesto o no  \n  ")
año=int(input("Ingresa el año  : "))#Input por ingreso de valores enteros 

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es bisiesto.")
else:
    print(f"{año} no es bisiesto.")

print("   ------GRACIAS  -----")
