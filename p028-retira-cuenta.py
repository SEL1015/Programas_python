# p028-retira-cuenta.py
# Simula un retiro de dinero de una cuenta con validaciones anidadas
print("\033[2J\033[H")
print("Bienvenido al Cajero Automático \n")


#Variables y entrada de datos 
saldo_actual = 1500.00
print(f"Tu saldo actual es: ${saldo_actual:,.2f}")

cantidad_retiro = float(input("Ingresa la cantidad a retirar: $"))
if cantidad_retiro > 0:
    if cantidad_retiro <= saldo_actual:
        nuevo_saldo = saldo_actual - cantidad_retiro
        print("\n Retiro exitoso.")
        print(f"Tu nuevo saldo es: ${nuevo_saldo:,.2f}")
    else:
        # Si la cantidad es válida pero excede el saldo
        print("\n Fondos insuficientes. No se puede completar la transacción.")
else:
    print("\n La cantidad a retirar debe ser un número positivo.")
print("\nGracias por usar nuestro servicio.")