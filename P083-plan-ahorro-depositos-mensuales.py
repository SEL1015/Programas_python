# P083-plan-ahorro-depositos-mensuales
"""
El programa simulará un plan de ahorro. Deberá solicitar al usuario un monto inicial, un depósito mensual fijo,
una tasa de interés mensual (porcentaje), y el número total de meses del plan. El programa debe mostrar una
tabla que detalle, para cada mes, el saldo inicial, el interés ganado en ese mes, y el saldo final. El interés se calcula
sobre el saldo inicial antes de sumar el nuevo depósito.
"""

print("\033[H\033[J")

# ENTRADA DE DATOS 


print("\n ---     PLAN DE AHORRO   --- ")
print("--------------------------------------------------------------------")
# Entrada de datos
monto_inicial = float(input(" 💵💵💵💵Monto inicial de ahorro :💸💵💵 "))
dep_mensual = float(input("Deposito mensual: 💰💰💰💰 "))
tasamen = float(input("Ingrese la tasa de interes mensual % : 🔣 "))
# Numero de meses a simular  
meses = int(input("Numero de meses a simular : "))

# Convertir porcentaje a decimal
tasamen = tasamen / 100

saldo = monto_inicial

print("\n Mes | Saldo Inicial | Interés | Saldo Final")
print("---------------------------------------------")

# Ciclo FOR para calcular cada mes
for mes in range(1, meses + 1):

    monto_inicial = saldo
    interes = monto_inicial * tasamen
    saldo_final = monto_inicial + interes + dep_mensual

    print("Mes {:<3} | Saldo Incial $ {:<10.2f} |  Interes $ {:<10.2f} | Saldo Final  $ {:<10.2f}".format(mes, monto_inicial, interes,saldo_final ))

    saldo = saldo_final

# Resultado final
print(F"\nSaldo total después de {meses},tendras : {saldo :<10.2f}")