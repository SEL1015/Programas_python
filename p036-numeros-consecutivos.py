#p036-numeros-consecutivos.py
#Problema: Escribe un programa que reciba tres números enteros y determine si son consecutivos. Si lo son,muestra un mensaje de confirmación; de lo contrario, informa que no lo son.
#Ejemplo de ejecución:
#Entrada: 9, 10, 11 
# Salida: Los números son consecutivos.
# Entrada: 1, 4, 6
# Salida: Los números no son consecutivos

print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")

#Entrada de datos 

print("Ingresa tres numeros entereos separados por un espacio : ")

#Declaracion de Variaables
num1,num2,num3 = input().split()# .split separa por un espacio 

#Asignar para determinar si son consecutivos 

num1,num2,num3= int(num1),int(num2),int(num3)   

#Evaluar si son consecuitivos con sentencias 

if num2 == num1 + 1 and num3 == num2 + 1:
    print("Los números son consecutivos.")
else:
    print("Los números no son consecutivos.")