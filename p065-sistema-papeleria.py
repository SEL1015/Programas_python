"""p065-SistemaPapeleria
Objetivo:
Desarrollar un sistema para gestionar las ventas de fotocopias en una papelería.
El programa registra múltiples ventas, calcula subtotales por tipo de copia,
aplica descuento por volumen (10% si la transacción supera 50 copias)
y muestra un resumen general con clasificación del desempeño del día.
Autor:Selena Ruiz Delgado 
Fecha : Jueves 26 de febrero del 2026
"""


print('\033[H\033[J')
print("-----------------------------")
print("🔖📱📖📖📖📖📖📖📖🔖")
print("Papelería la Malena, SA. de CV 📋")
print("Sistema de ventas de copias")
print("-----------------------------")

#DECLARACION DE VARIABLES A UTILIZAR 
ventas=0
subtotal=0
cantidad_c=0
cantidad_o=0
cantidad_d=0
cantidad_p=0
total_c = total_o = total_d = total_p=0
while True:
    nombre=input("Dame tu nombre")
    print(f"Hola {nombre} !BIENVENIDO !🐝🐝🐝🐝 ")
    ventas+=1
    print(f"Venta {ventas}")
    tipo= input("Tipo de copia  (C)arta $3 \n, (O)ficio $4  , \n (D)oble Of $6 , \n (P)lano $12 \n  Tipo de copia  requerida ?"). upper()

    if tipo not in "CODP":
        print("Error: Tipo de copia no valido.Intenta de nuevo")
        ventas-=1
        continue
    cantidad=int(input("Cantidad  ?"))
    if tipo=="C":
        cantidad_c+=1
        total_c+=cantidad*3
    elif tipo=="O":
        cantidad_o +=1
        total_o +=cantidad*4
    elif tipo =="D":
        cantidad_d +=1
        total_d +=cantidad*6
    elif tipo=="P":
        cantidad_p +=1
        total_p +=cantidad*12

    if input ("OTRA VENTA (S/N)?").upper() !="S":  break
total_copias = cantidad_c + cantidad_o + cantidad_d + cantidad_p
total_ventas=total_c + total_o + total_d + total_p


if total_copias>50:
    total_ventas*=0.90

print("📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄📄")
print("---------------------------------------")
print("Resumen diario de ventas")
print("--------------------------------------- ")
print(f"Ventas realizadas : {ventas} ")
print("--------------------------------------- ")
print(f"Carta :            {cantidad_c:2d}       - $ {total_c:8.2f} ")
print(f"Oficio :           {cantidad_o:2d}       - $ {total_o:8.2f} ")
print(f"Doble Oficio :     {cantidad_d:2d}       - $ {total_d:8.2f} ")
print(f"Plano :            {cantidad_p:2d}       - $ {total_p:8.2f} ")
print(f"Total de Ventas\t: {total_copias:2d}     - $ {total_ventas:8.2f}")

mensaje =""
if total_ventas >150:
    mensaje="Venta Superada 👍"
elif total_ventas>= 50:
    mensaje="Venta Frecuente 😏"
else:
    mensaje="Venta Moderada 😊"

print(f"Esta Vneta es una : {mensaje}")
print("Gracias por su compra, !Vuelva Pronto!^_~")

print("♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️")