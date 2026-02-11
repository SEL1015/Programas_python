#p015-hipotenusa-triangulo 
#Calcular la hipotenusa de un triangulo con teorema de pitagoras  a^2 + b^2 = c^2
# Entrada
print("\033[h\033[j")#imprime una secuencia ansi que borra la pantalla]]")
import math  ##Se importa la libreria math para usar la funcion hypot

print("Calcular la hipotenusa de un triangulo con teoream de pitagoras")
lado1=float(input("Ingrese la longitud del primer lado del triangulo:"))
lado2=float(input("Ingrese la longitud del segundo lado del triangulo:"))
hipotenusa = math.hypot(lado1,lado2) ##Uso la funcion hypot para abreviar el calculo de la hipotenusa

#Salida 
print(f"La hipotenusa del triangulo es : {hipotenusa:.4f}")


