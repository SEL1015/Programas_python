#p103-ciudades
"""
Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:
• Cuántos elementos tiene la lista.
• La lista completa.
• La lista ordenada en orden descendente.
• Cuántas ciudades inician con una letra consonante y sus nombres.
Ejemplo:
Introduzca nombre de ciudad ($ para detener): Aguascalientes
Introduzca nombre de ciudad ($ para detener): Monterrey
Introduzca nombre de ciudad ($ para detener): Oaxaca
Introduzca nombre de ciudad ($ para detener): Saltillo
Introduzca nombre de ciudad ($ para detener): $
--- Resultados ---
Total de ciudades introducidas: 4
Lista original: ['Aguascalientes', 'Monterrey', 'Oaxaca', 'Saltillo']
Lista ordenada descendente: ['Saltillo', 'Oaxaca', 'Monterrey', 'Aguascalientes']
Ciudades que inician con consonante: 2
Lista de ciudades con consonante inicial: ['Monterrey', 'Saltillo']
"""

ciudades = []
print('\033[H\033[J')
while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ")
    
    if ciudad == "$":
        break
    
    ciudades.append(ciudad)

orden_desc = sorted(ciudades, reverse=True)

consonantes = []
vocales = "AEIOUaeiou"

for ciudad in ciudades:
    if len(ciudad) > 0 and ciudad[0] not in vocales:
        consonantes.append(ciudad)

print("--- Resultados ---")
print("Total de ciudades introducidas:", len(ciudades))
print("Lista original:", ciudades)
print("Lista ordenada descendente:", orden_desc)
print("Ciudades que inician con consonante:", len(consonantes))
print("Lista de ciudades con consonante inicial:", consonantes)

print("GRACIAS POR PARTICIPAR")