#p021-distancia-entre-puntos
#Calcular la distancia entre dos puntos en el plano castesiano
# El programa debe pedir al usuario que ingrese las coordenadas (x,y) del punto A y las coordenadas (x,y) del punto B. Utiliza la siguiente fórmula para 
#calcular la distancia: 

#Entrada de datos
import math
print("Calcular la distancia entre dos puntos en el plano cartesiano")
print("Ingresar coordenadas del punto A separadas por espacio (XA YA):")
#Define variables para almacenar las cordenadas del punto A y B 
XA, YA= input().split()
XA, YA=float(XA), float(YA)
#Solciitud de coordenadas para el punto B 
print("Ingresar coordenadas del punto B separadas por espacio (xB yB):")
XB, YB= input().split()
XB, YB=float(XB), float(YB)

#Calculo de distancia entre los puntos A y B utilizando la formula de distancia entre dos puntos en el plano cartesiano
distancia=math.sqrt((XB-XA)**2 + (YB-YA)**2)

#Salida de datos 
print(f"La distancia entre los puntos A {XA,YA} Y B{XB,YB} es : {distancia:.4f}")

#Fin del programa 
