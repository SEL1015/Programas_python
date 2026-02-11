#p018-area-volumen-cilindro 
#Calcular el area y volumen de un cilindro

#Entrada
print("Calcular el area y volumen de un circulo")

import math
PI= 3.1416
radio=float(input("Ingresa el radio del circulo:"))
altura= float(input("Ingresa la altura del circulo:"))

#Calculo del area y volumen del circulo
Area = PI * radio * (radio + altura) 
Volumen = PI * (radio * radio) * altura 

#Salida de datos

print(f"(El area del circulo es: {Area:.2f}")
print(f"(El volumen del circulo es: {Volumen:.2f}")

