# p027-calcular-paga-extra.py
# Calcula la paga de un trabajador considerando horas extra.
print("\033[2J\033[H")


print('Calculando la paga de un trabajador considerando las horas extras al doble ')


# Entrada de datos
print("Dame los Datos del trabajador: ")
nombre = input("Nombre del trabajador: ")
horas = int(input("Horas trabajadas: "))
paga_hora = float(input('Paga por hora: '))


horas_normales=horas if horas < 40 else 40 #If de corto cicuito 
paga_normal=horas_normales *paga_hora

# Cálculo de la paga
horas_normales = 40
paga_normal = horas_normales * paga_hora
horas_extra = paga_extra = 0

if horas > 40:
    horas_extra = horas - 40
    paga_extra = horas_extra * (paga_hora * 2)
    total = paga_normal + paga_extra

else: 
    total = paga_normal

print("\n Cálculo completado.")
print(f'\nEl trabajador {nombre} tiene {horas_normales} horas normales + {horas_extra} horas extra.')
print(f'Paga normal = ${paga_normal:13,.2f}')
print(f'Paga extra = ${paga_extra:13,.2f}')
print(f'El pago total = ${total:13,.2f}')# , separador de miles 



print('\n* ¡Programa finalizado! *')