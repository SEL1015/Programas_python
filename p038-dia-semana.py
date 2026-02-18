#p038-dia-semana.py
#Problema: Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana correspondiente, considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango,
#debe mostrar un mensaje de error.
#Ejemplo de ejecución:
# Entrada: 2
# Salida: Lunes
# Entrada: 8
# Salida: Error: Día inválido.

print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")  

#Entrada de datos  
print("Ingresa un numero del 1 al 7 ")

#Declaracion de variables 
numerosem = int(input())#convertir a entero    

#Evaluar el numero con sentencias if/elif
if numerosem == 1:
    print("Domingo")
elif numerosem== 2:
    print("Lunes")
elif numerosem == 3:
    print("Martes")
elif numerosem==4:
    print("Miercoles")
elif numerosem ==5:
    print("Jueves")
elif numerosem == 6:
    print("Viernes")
elif numerosem == 7 :
    print("Sabado")
else:
    print("Error: Día inválido.")
print("Fin del programa.")

