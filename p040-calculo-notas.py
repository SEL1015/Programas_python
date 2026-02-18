#p040-calculo-notas.py
#Problema: Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario. Basado en el
#promedio, el programa deberá mostrar uno de los siguientes mensajes:
# Menor a 6: "Quedas reprobado"
#Desde 6 hasta menos de 7: "Pasas de panzazo"
#Desde 7 hasta menos de 8: "Muy bien, puedes mejorar"
#Desde 8 hasta menos de 9: "Excelente, sigue así"
#Desde 9 hasta 10: "Perfecto, tu esfuerzo valió la pena"

print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]")

#Entrada de datos
print("Ingresa cinco calificaciones separadas por un espacio del  1 al 10 :")
#Declaracion de variables
cal1,cal2,cal3,cal4,cal5 = input().split()# .split separa por un espacio

#Asignar para determinar el promedio
cal1,cal2,cal3,cal4,cal5 = int(cal1),int(cal2),int(cal3),int(cal4),int(cal5) # Convertir a entero los numeros ingresados

promedio = (cal1 + cal2 + cal3 + cal4 + cal5) / 5   
#Evaluar el promedio con sentencias if/elif
print(f"Tu promedio es: {promedio:.2f}") # Imprime el promedio con dos decimales
if promedio <6:
    print("Quedas reprobado")
elif promedio >= 6 and promedio < 7:
    print("Pasas de panzazo")   
elif promedio >= 7 and promedio < 8:
    print("Muy bien, puedes mejorar")
elif promedio >= 8 and promedio < 9:
    print("Excelente sigue asi ")
elif promedio >= 9 and promedio < 10:
    print("Perfecto, tu esfuerzo valio la pena")
else:
    print("Error: Promedio inválido.")


