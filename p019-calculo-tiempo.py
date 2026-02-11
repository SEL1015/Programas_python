##p019-calculo-tiempo
#Diseña un programa que tome una cantidad de horas como un número entero y convierta a minutos y segundos

#Entrada
print("Convertir horas a minutos y segundos considerando :")
print("1 hora=60 minutos")
print("1 minuto =60 segundos")
print("1 dia=24 horas")

#Definir cantidad a convertir 
hora=int(input("Ingrese la cantidad de horas a converir "))

#Calculo de minutos y segundos 
minutos = hora*60
segundo =minutos*60
dia = hora/24
#Salida de datos 

print(f" {hora} horas equivalen a  {minutos:.2f} minutos")
print(f" {hora}  horas equivalen a {segundo:.2f} segundoos")
print(f" {hora}  horas equivalen a {dia:.2f}     dias")

