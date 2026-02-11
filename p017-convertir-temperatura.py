#p017-convertir-temperatura
#Convertir la temperatura de grados Celsius a grados Fahrenheit.

#Entrada de datos
print("Convertir la temperatura de grados Celsius a grados Fahrenheit.")
celcius= float(input("Ingrese la temperatura en grados Celcius:"))

#Calculo de la temperatura en grados Fahrenheit
fahrenheit= (celcius * 9/5)+32


#Salida de datos obtenidos 
print("La temperatura en grados Fahrenheit es:{fahrenheit:.2f} °f".format(fahrenheit=fahrenheit))
