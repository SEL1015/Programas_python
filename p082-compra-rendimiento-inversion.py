#TAREA 4 
#p082-compra-rendimiento-inversion
"""
Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años. El usuario
debe ingresar el monto inicial y la tasa de interés anual (porcentaje) para cada uno de los dos fondos, así como
el número de años a proyectar. El programa deberá mostrar una tabla comparativa anual y al final indicar qué fondo
generó un mayor rendimiento.
"""

print("\033[H\033[J")

# ENTRADA DE DATOS 


print("\n ---     Fondo de Inversión A    --- ")
print("--------------------------------------------------------------------")
# Entrada de datos
monto1 = float(input("Ingrese el monto inicial del Fondo A: "))
tasa1 = float(input("Ingrese la tasa anual (%) del Fondo A: "))

print("\n ---     Fondo de Inversión B   --- ")
monto2 = float(input("Ingrese el monto inicial del Fondo B: "))
tasa2 = float(input("Ingrese la tasa anual (%) del Fondo B: "))
# Numero de años a proyectar ña inversion 
anios = int(input("Ingrese el número de años a proyectar: "))

# Convertir porcentaje a decimal
tasa1 = tasa1 / 100
tasa2 = tasa2 / 100


print("-----Comparacion de rendimientos anuales----")
print("Año | Fondo A     | Fondo B")
print("-------------------------------------")

# Ciclo FOR para calcular cada año
for i in range(1, anios + 1):

    monto1 = monto1 + (monto1 * tasa1)
    monto2 = monto2 + (monto2 * tasa2)

    print("{:<3} | $ {:<10.2f} | $ {:<10.2f}".format(i, monto1, monto2))

# Comparación final
print("\nResultado final:")

if monto1 > monto2:
    print("El Fondo A (${:0.2f}) superó al Fondo B (${:0.2f}).".format(monto1, monto2))
elif monto1> monto2:
    print("El Fondo A (${:0.2f}) superó al Fondo B (${:0.2f}).".format(monto1, monto2))
else:
    print("Ambos fondos terminaron con el mismo rendimiento.")