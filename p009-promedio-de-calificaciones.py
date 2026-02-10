#p009-promedio-de-calificaciones.py
#Calcula el promedio de tres calificaciones ingresadas por el usuario
#Entrada
print("Dame 3 calificaciones separadas por espacio:\n")


#Solicitar las calificaciones en una sola linea separadas por espacio 
print("Dame 3 calificaciones separadas por espacios:\n")

cal1,cal2,cal3=input().split()
cal1,cal2,cal3=int(cal1),int(cal2) , int (cal3)

#Calcular el promedio 
promedio=(cal1+cal2+cal3)/3

#Mostrar el resultado 

print(f"Las calificaciones fueron {cal1}, {cal2}, {cal3}")

print(f"El promedio de las calificaciones es: {promedio}")
