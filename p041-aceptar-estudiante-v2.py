#p041-aceptar-estudiante-v2
#Problema: La "Universidad Kitty Kat SA" solo acepta estudiantes que cumplan con los siguientes requisitos: ser
#mujer, ser mayor de 21 años y tener un promedio entre 8 y 9.5.
#Escribe un programa que solicite el nombre, sexo (h/m), edad y tres calificaciones de un aspirante. El programa
#debe evaluar los datos y mostrar un mensaje claro que indique si el estudiante fue aceptado. Si no es aceptado, el mensaje debe especificar la razón del rechazo (ya sea por no cumplir con el sexo, la edad o el promediorequerido).
#Ejemplos de ejecución:
#Entrada: Nombre: Maria, Sexo: m, Edad: 22, Calificaciones: 10, 9, 8.5
#Salida: ¡Felicidades, Maria! Has sido aceptada. Cumples con la edad y tu promedio de 9.17 está dentro delrango permitido.
#Entrada: Nombre: Jose, Sexo: h, Edad: 21, Calificaciones: 7, 6, 5
# Salida: Lo sentimos, Jose. La universidad solo acepta mujeres.
# Entrada: Nombre: Dolores, Sexo: m, Edad: 20, Calificaciones: 10, 10, 10
# Salida: Lo sentimos, Dolores. No cumples con la edad requerida (mayores de 21 años).
# Entrada: Nombre: Sandra, Sexo: m, Edad: 25, Calificaciones: 7, 6, 5
# Salida: Lo sentimos, Sandra. Tu promedio de 6.0 no alcanza el mínimo requerido de 8.

print("\033[H\033[J")#imprime una secuencia ansi que borra la pantalla]]") 

#Entrada de datos
print("La Universidad Kitty Kat SA solo acepta estudiantes que cumplan con los siguientes requisitos:")
print("ser mujer, ser mayor de 21 años y tener un promedio entre 8 y 9.5. ")

#Declaracion de variables
nombre=input("Ingresa tu nombre : " )
sexo=input("Ingresa tu sexo (h/m) : " ).lower()##acepta minusculas 


#Evaluar con sentencias if/elif
if sexo != 'm':
    print(f"Lo sentimos, {nombre}. La universidad solo acepta mujeres.")
else:
    edad=int(input("Ingresa tu edad : "))#Input por ingreso de valores enteros 
    if edad < 22:
        print(f"Lo sentimos, {nombre}. No cumples con la edad requerida (mayores de 22 años).")
    else:
        #Solicitar las calificaciones
        print("Ingresa tus tres calificaciones separadas por un espacio : ")
        cal1,cal2,cal3 = input().split()# .split separa por un espacio lo solicita por espacios si 

        #Asignar para determinar el promedio
        cal1,cal2,cal3 = int(cal1),int(cal2),int(cal3) # Convertir a entero los numeros ingresados 
        promedio = (cal1 + cal2 + cal3) / 3
        if promedio < 8:
            print(f"Lo sentimos, {nombre}. Tu promedio de {promedio:.2f} no alcanza el mínimo requerido de 8.")
        else: 
            print(f"¡Felicidades, {nombre}! Has sido aceptada. Cumples con la edad y tu promedio de {promedio:.2f} está dentro del rango permitido.")
print("Fin del programa.")

##Mofique prorgrama 
