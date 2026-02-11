#p022-resistencia-equivalente-paralelo 
#Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo. 
#El programa debe solicitar al usuario que ingrese el valor de cada una de las cuatro resistencias (R1, R2, R3 y R4). 
#Luego, debe calcular la resistencia total usando la siguiente fórmula: 

#Entrada de datos 
print("Calcular la resistencia total de un circuito con cuatro resistencias en paralelo")
#definir variables 
R1=float(input("Ingresa el valor de la resistencia R1 en Ohms:"))
R2=float(input("Ingresa el valor de la resistencia R2 en Ohms:"))
R3=float(input("Ingresa el valor de la resistencia R3 en Ohms:"))
R4=float(input("Ingresa el valor de la resistencia R4 en Ohms:"))

#Calculo de la resistencia total utilizando la formula de la resitencia en paralelo
#Agregar las formulas correspondientes 
resistencia_paralelo= 1//((1/R1) + (1/R2)+(1/R3)+(1/R4))

#Salida de datos
#Impresion de los resultados obtenidos 
print(f"La resitencia total del ciurcuito con resistencias en paralelo es: {resistencia_paralelo:.4f} Ohms")

#Fin del programa 


