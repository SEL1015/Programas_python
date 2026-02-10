#p14-funciones-trigonometricas
#DEMOSTRAR LAS FUNCIONES TRIGONOMETRICAS


import math as mt

print("Demostrar el uso de funciones trigonometrias")

angulo= 90 #grados
radianes= mt.radians(angulo)

seno=mt.sin(radianes)
coseno= mt.cos(radianes)
tangente= mt.degrees(radianes)



grados=mt.degrees(radianes)#a grados 

salida=("Resumen de funciones /n"
f"Seno   :   {seno:.4f}\n"
f"Coseno   :   {coseno:.4f}\n"
f"Tangente   :   {tangente:.4f}\n"
f"El angulo {angulo:.4f} grados , en radianes equivale a {radianes:.4f}\n"
f"los radianes {angulo:.4f} radianes , equivalen a {grados:.1f}\n"
)#Mostar la salida formateada

print(salida)