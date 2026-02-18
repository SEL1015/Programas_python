# p037-numero-mayor.py
#escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.
#Ejemplo de ejecución:
#Entrada: 11, 30, -1
#Salida: El número mayor es 30.


print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")

#Entrada de datos

print("Ingresa tres numeros enteros separados por un espacios :")

#Declaracion de variables
numero1,numero2,numero3 = input().split()# .split separa por un espacio

#Asignar para determinar cual es el mayor
numero1,numero2,numero3= int(numero1),int(numero2),int(numero3)

#Evaluar cual es el mayor con sentencias if/elif
if numero1 >= numero2 and numero1 >= numero3:
    print(f"El número mayor es {numero1}.") 
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El número mayor es {numero2}.")     
elif numero3 >= numero1 and numero3 >= numero2:
    print(f"El número mayor es {numero3}.")

print("Fin del programa.")

